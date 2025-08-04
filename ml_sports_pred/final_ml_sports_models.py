import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, KFold, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_predict
import warnings
warnings.filterwarnings('ignore')

# Load and prepare data
df = pd.read_csv('home_team_model_f.csv')
desired_col = ['FTR','AvgH', 'AvgD', 'AvgA', 'prob_home', 'prob_draw', 'prob_away',
           'overround', 'home_away_odds_ratio', 'home_away_prob_diff',
           'implied_home_goals', 'HT_AvgGoalsScored_Season',
           'HT_AvgGoalsConceded_Season', 'AT_AvgGoalsScored_Season',
           'AT_AvgGoalsConceded_Season']

df = df[desired_col]

# Feature columns
feature_cols = ['AvgH', 'AvgD', 'AvgA', 'prob_home', 'prob_draw', 'prob_away',
           'overround', 'home_away_odds_ratio', 'home_away_prob_diff',
           'implied_home_goals', 'HT_AvgGoalsScored_Season',
           'HT_AvgGoalsConceded_Season', 'AT_AvgGoalsScored_Season',
           'AT_AvgGoalsConceded_Season']

# Convert feature columns to numeric
df[feature_cols] = df[feature_cols].apply(pd.to_numeric, errors='coerce')
df.dropna(inplace=True)

print("Original dataset shape:", df.shape)
print("FTR values:", df['FTR'].unique())

# Encode target variable
le = LabelEncoder()
df['FTR'] = le.fit_transform(df['FTR'])
print("Label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))

# =============================================================================
# FEATURE ENGINEERING
# =============================================================================

# 1. Create interaction features
df['prob_home_away_ratio'] = df['prob_home'] / (df['prob_away'] + 1e-8)  # Avoid division by zero
df['goals_difference'] = df['HT_AvgGoalsScored_Season'] - df['AT_AvgGoalsScored_Season']
df['defensive_difference'] = df['AT_AvgGoalsConceded_Season'] - df['HT_AvgGoalsConceded_Season']
df['home_form'] = df['HT_AvgGoalsScored_Season'] - df['HT_AvgGoalsConceded_Season']
df['away_form'] = df['AT_AvgGoalsScored_Season'] - df['AT_AvgGoalsConceded_Season']
df['form_difference'] = df['home_form'] - df['away_form']

# 2. Additional football-specific features
df['total_goals_expected'] = df['HT_AvgGoalsScored_Season'] + df['AT_AvgGoalsScored_Season']
df['home_advantage'] = df['prob_home'] - df['prob_away']
df['market_confidence'] = 1 - df['overround']
df['draw_factor'] = df['prob_draw'] / (df['prob_home'] + df['prob_away'] + 1e-8)

# 3. Squared terms for important features
df['prob_home_sq'] = df['prob_home'] ** 2
df['prob_away_sq'] = df['prob_away'] ** 2
df['home_away_ratio_sq'] = df['home_away_odds_ratio'] ** 2

# Update feature list
enhanced_features = feature_cols + [
    'prob_home_away_ratio', 'goals_difference', 'defensive_difference',
    'home_form', 'away_form', 'form_difference', 'total_goals_expected',
    'home_advantage', 'market_confidence', 'draw_factor',
    'prob_home_sq', 'prob_away_sq', 'home_away_ratio_sq'
]

# Prepare data
X = df[enhanced_features].values
y = df['FTR'].values

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Cross-validation setup
kf = KFold(n_splits=10, shuffle=True, random_state=42)

print(f"\nEnhanced dataset shape: {X.shape}")
print(f"Class distribution: {np.bincount(y)}")

# =============================================================================
# MODEL COMPARISON
# =============================================================================

print("\n" + "="*60)
print("MODEL COMPARISON WITH ENHANCED FEATURES")
print("="*60)

# 1. Baseline models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Logistic (Balanced)': LogisticRegression(max_iter=1000, class_weight='balanced'),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
    'Random Forest (Balanced)': RandomForestClassifier(n_estimators=100, max_depth=10, 
                                                       class_weight='balanced', random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, max_depth=6, random_state=42),
    'SVM': SVC(probability=True, random_state=42),
    'Neural Network': MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
}

model_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=kf, scoring='accuracy')
    model_results[name] = scores
    print(f"{name:20s}: {np.mean(scores):.4f} ± {np.std(scores):.4f}")

# =============================================================================
# HYPERPARAMETER TUNING FOR BEST MODELS
# =============================================================================

print("\n" + "="*60)
print("HYPERPARAMETER TUNING")
print("="*60)

# Tune Random Forest
rf_params = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'class_weight': [None, 'balanced']
}

rf_grid = GridSearchCV(RandomForestClassifier(random_state=42), rf_params, 
                       cv=5, scoring='accuracy', n_jobs=-1)
rf_grid.fit(X_scaled, y)

print(f"Best Random Forest: {rf_grid.best_score_:.4f}")
print(f"Best params: {rf_grid.best_params_}")

# Tune Gradient Boosting
gb_params = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2]
}

gb_grid = GridSearchCV(GradientBoostingClassifier(random_state=42), gb_params, 
                       cv=5, scoring='accuracy', n_jobs=-1)
gb_grid.fit(X_scaled, y)

print(f"Best Gradient Boosting: {gb_grid.best_score_:.4f}")
print(f"Best params: {gb_grid.best_params_}")

# Tune Logistic Regression
lr_params = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear', 'saga'],
    'class_weight': [None, 'balanced']
}

lr_grid = GridSearchCV(LogisticRegression(max_iter=1000), lr_params, 
                       cv=5, scoring='accuracy', n_jobs=-1)
lr_grid.fit(X_scaled, y)

print(f"Best Logistic Regression: {lr_grid.best_score_:.4f}")
print(f"Best params: {lr_grid.best_params_}")

# =============================================================================
# ENSEMBLE METHODS
# =============================================================================

print("\n" + "="*60)
print("ENSEMBLE METHODS")
print("="*60)

# Create ensemble with best models
ensemble_soft = VotingClassifier([
    ('lr', lr_grid.best_estimator_),
    ('rf', rf_grid.best_estimator_),
    ('gb', gb_grid.best_estimator_)
], voting='soft')

ensemble_hard = VotingClassifier([
    ('lr', lr_grid.best_estimator_),
    ('rf', rf_grid.best_estimator_),
    ('gb', gb_grid.best_estimator_)
], voting='hard')

# Test ensembles
ensemble_soft_scores = cross_val_score(ensemble_soft, X_scaled, y, cv=kf)
ensemble_hard_scores = cross_val_score(ensemble_hard, X_scaled, y, cv=kf)

print(f"Ensemble (Soft):     {np.mean(ensemble_soft_scores):.4f} ± {np.std(ensemble_soft_scores):.4f}")
print(f"Ensemble (Hard):     {np.mean(ensemble_hard_scores):.4f} ± {np.std(ensemble_hard_scores):.4f}")

# =============================================================================
# FEATURE SELECTION
# =============================================================================

print("\n" + "="*60)
print("FEATURE SELECTION")
print("="*60)

# Select best features
selector = SelectKBest(f_classif, k=15)
X_selected = selector.fit_transform(X_scaled, y)

# Test with selected features
selected_features = np.array(enhanced_features)[selector.get_support()]
print(f"Selected features: {list(selected_features)}")

# Test best model with selected features
best_model_selected = cross_val_score(rf_grid.best_estimator_, X_selected, y, cv=kf)
print(f"Best model with selected features: {np.mean(best_model_selected):.4f} ± {np.std(best_model_selected):.4f}")

# =============================================================================
# FINAL RESULTS
# =============================================================================

print("\n" + "="*60)
print("FINAL RESULTS SUMMARY")
print("="*60)

# Get best overall model
best_scores = [
    ('Original Logistic', np.mean(model_results['Logistic Regression'])),
    ('Tuned Random Forest', rf_grid.best_score_),
    ('Tuned Gradient Boosting', gb_grid.best_score_),
    ('Tuned Logistic', lr_grid.best_score_),
    ('Ensemble Soft', np.mean(ensemble_soft_scores)),
    ('Ensemble Hard', np.mean(ensemble_hard_scores)),
    ('RF with Feature Selection', np.mean(best_model_selected))
]

best_scores.sort(key=lambda x: x[1], reverse=True)
print("Model Rankings:")
for i, (name, score) in enumerate(best_scores, 1):
    print(f"{i}. {name:25s}: {score:.4f}")

# Detailed analysis of best model
best_model = ensemble_soft if np.mean(ensemble_soft_scores) > rf_grid.best_score_ else rf_grid.best_estimator_
best_model_name = "Ensemble (Soft)" if np.mean(ensemble_soft_scores) > rf_grid.best_score_ else "Tuned Random Forest"

print(f"\nBest Model: {best_model_name}")
y_pred = cross_val_predict(best_model, X_scaled, y, cv=kf)

print("\nConfusion Matrix:")
cm = confusion_matrix(y, y_pred)
print("       A    D    H")
for i, row_label in enumerate(['A', 'D', 'H']):
    print(f"{row_label}   {cm[i,0]:4d} {cm[i,1]:4d} {cm[i,2]:4d}")

print(f"\nClassification Report:")
print(classification_report(y, y_pred, target_names=['Away', 'Draw', 'Home']))

# Calculate improvement
original_score = np.mean(model_results['Logistic Regression'])
best_score = np.mean(ensemble_soft_scores) if np.mean(ensemble_soft_scores) > rf_grid.best_score_ else rf_grid.best_score_
improvement = best_score - original_score

print(f"\nImprovement Summary:")
print(f"Original Logistic Regression: {original_score:.4f}")
print(f"Best Model:                   {best_score:.4f}")
print(f"Improvement:                  {improvement:.4f} ({improvement/original_score*100:.1f}%)")
print(f"Improvement over random:      {best_score - 1/3:.4f} ({(best_score - 1/3)/(1/3)*100:.1f}%)")

# Feature importance for Random Forest
if hasattr(rf_grid.best_estimator_, 'feature_importances_'):
    print(f"\nTop 10 Most Important Features (Random Forest):")
    importances = rf_grid.best_estimator_.feature_importances_
    feature_importance = list(zip(enhanced_features, importances))
    feature_importance.sort(key=lambda x: x[1], reverse=True)
    
    for i, (feature, importance) in enumerate(feature_importance[:10], 1):
        print(f"{i:2d}. {feature:25s}: {importance:.4f}")
