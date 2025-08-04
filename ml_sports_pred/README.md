# Sports Match Outcome Prediction Model

A machine learning system for predicting football match outcomes using historical data and betting odds analysis.

## 🎯 Project Overview

This project implements a comprehensive machine learning pipeline to predict football match results (Home/Draw/Away) using ensemble methods and advanced feature engineering. The model analyzes betting odds, team performance metrics, and derived statistical features to achieve meaningful predictive performance in the challenging domain of sports analytics.

## 📊 Key Results

- **Accuracy**: 50.7% (52% improvement over random guessing)
- **Best Model**: Ensemble voting classifier combining Logistic Regression, Random Forest, and Gradient Boosting
- **Key Finding**: Home advantage emerges as the strongest predictor (15.15% feature importance)
- **Dataset**: 7,045 matches with 27 engineered features

## 🛠️ Technical Implementation

### Models Tested
- Logistic Regression (with hyperparameter tuning)
- Random Forest
- Gradient Boosting
- Support Vector Machine
- Neural Network
- Ensemble Methods (Soft/Hard Voting)

### Feature Engineering
- **Base Features**: Betting odds, team statistics, probabilities
- **Derived Features**: Home advantage, form differences, odds ratios
- **Advanced Features**: Squared terms, probability ratios, market confidence

### Key Features Identified
1. Home Advantage (15.15%)
2. Implied Home Goals (9.69%)
3. Home/Away Probability Ratio (8.59%)
4. Home/Away Odds Ratio (7.54%)
5. Probability Differences (6.84%)

## 📁 Project Structure

```
├── home_team_model_f.csv          # Main dataset
├── sports_prediction_model.py     # Main analysis script
└── README.md                     # This file
```

## 📊 Data Source

Historical football data sourced from [Football-Data.co.uk](https://www.football-data.co.uk/data.php), which provides comprehensive match statistics and betting odds for multiple European leagues.

### Required Data Features
- Match results (FTR)
- Betting odds (Home/Draw/Away)
- Team performance metrics
- Goals scored/conceded averages

## 🔍 Model Performance

| Model | Accuracy | Std Dev |
|-------|----------|---------|
| Tuned Logistic Regression | 50.70% | ±1.49% |
| Ensemble (Soft Voting) | 50.55% | ±1.74% |
| Ensemble (Hard Voting) | 50.52% | ±1.77% |
| Original Logistic | 50.48% | ±1.86% |
| Random Forest | 50.22% | ±1.49% |

### Confusion Matrix Analysis
- **Home Win Prediction**: 89% recall (strong performance)
- **Away Win Prediction**: 40% recall (moderate performance)
- **Draw Prediction**: ~0% recall (major limitation)

## 🎯 Key Insights

### Model Strengths
- Successfully identifies home advantage patterns
- Consistent performance across cross-validation folds
- Significantly outperforms random guessing
- Clear feature importance interpretability

### Limitations
- Poor draw prediction capability
- Home win bias in predictions
- Inherent unpredictability of sports outcomes
- Limited by available features

### Business Applications
- Sports analytics and betting insights
- Team performance evaluation
- Market odds validation
- Statistical sports journalism

## 🔧 Future Improvements

- **Additional Features**: Player injuries, weather conditions, referee statistics
- **Advanced Models**: Deep learning approaches, time series analysis
- **Real-time Data**: Live odds and in-game statistics
- **League-specific Models**: Separate models for different competitions
- **Draw Prediction**: Specialized approaches for draw outcomes

## 📋 Requirements

```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
warnings
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Football-Data.co.uk](https://www.football-data.co.uk/) for providing comprehensive historical football data
- The scikit-learn community for excellent machine learning tools
- Sports analytics research community for methodology insights

## 📞 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/sports-prediction-model](https://github.com/yourusername/sports-prediction-model)

---

⭐ **Star this repository if you found it helpful!**
