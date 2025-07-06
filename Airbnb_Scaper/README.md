# Airbnb Scraper

A Python web scraper for extracting Airbnb listing data using Selenium WebDriver. This tool automates the process of searching for accommodations and collecting listing information including titles, types, prices, reviews, and links.

## Features

- **Automated Search**: Search for Airbnb listings by location, dates, number of guests, and beds
- **Pagination Support**: Automatically navigates through multiple pages of results
- **CSV Export**: Saves scraped data to CSV format for easy analysis
- **Robust Error Handling**: Handles missing elements and timeouts gracefully
- **Customizable Filters**: Filter results by minimum number of beds

## Prerequisites

- Python 3.x
- Chrome browser installed
- ChromeDriver executable

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/airbnb-scraper.git
cd airbnb-scraper
```

2. Install required packages:
```bash
pip install selenium pandas
```

3. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/)
   - Download the version matching your Chrome browser
   - Update the path in the script:
   ```python
   os.environ['PATH'] += r"C:\path\to\your\chromedriver"
   ```

## Usage

### Basic Example

```python
from airbnb_scraper import search, scrape

# Search for listings
search(
    location="New York, NY",
    start="2024-12-01",
    end="2024-12-07", 
    num_adults=2,
    num_beds=1
)

# Scrape the results
scrape("airbnb_listings.csv")
```

### Function Parameters

#### `search(location, start, end, num_adults, num_beds)`

- `location` (str): City, state, or country to search
- `start` (str): Check-in date in YYYY-MM-DD format
- `end` (str): Check-out date in YYYY-MM-DD format
- `num_adults` (int): Number of adult guests
- `num_beds` (int): Minimum number of beds required

#### `scrape(file_name_to_save)`

- `file_name_to_save` (str): Name of the CSV file to save results

## Data Fields

The scraper extracts the following information for each listing:

| Field | Description |
|-------|-------------|
| `title` | Property name/title |
| `type` | Property type (apartment, house, etc.) |
| `price` | Nightly price |
| `reviews` | Number of reviews |
| `link` | Direct link to the listing |

## Sample Output

```csv
title,type,price,reviews,link
"Cozy Studio in Manhattan","Entire studio","$120","45",https://www.airbnb.com/rooms/123456
"Brooklyn Loft with View","Entire loft","$180","32",https://www.airbnb.com/rooms/789012
```

## Important Notes

### Legal and Ethical Considerations

- **Respect robots.txt**: Always check Airbnb's robots.txt file
- **Rate Limiting**: The script includes delays to avoid overwhelming servers
- **Terms of Service**: Ensure compliance with Airbnb's Terms of Service
- **Personal Use**: This tool is intended for personal research and educational purposes

### Technical Considerations

- **Dynamic Content**: Airbnb uses dynamic loading; the script includes appropriate waits
- **Element Selectors**: CSS selectors may change; update if scraping fails
- **Browser Updates**: Keep ChromeDriver updated with your Chrome version

## Troubleshooting

### Common Issues

1. **ChromeDriver Path Error**
   - Ensure ChromeDriver is in your PATH or update the script path
   - Verify ChromeDriver version matches your Chrome browser

2. **Element Not Found**
   - Airbnb may have updated their HTML structure
   - Check and update CSS selectors in the script

3. **Timeout Errors**
   - Increase wait times if you have a slow internet connection
   - Check if Airbnb is blocking automated requests

4. **Empty Results**
   - Verify search parameters are valid
   - Check if there are listings available for your criteria

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Disclaimer

This scraper is for educational and personal use only. Users are responsible for:
- Complying with Airbnb's Terms of Service
- Respecting rate limits and server resources
- Following applicable laws and regulations
- Using scraped data ethically and responsibly

The authors are not responsible for any misuse of this tool or any consequences arising from its use.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter issues or have questions:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

---

**Note**: Web scraping landscapes change frequently. This scraper was last tested on [current date]. If you encounter issues, the website structure may have changed and the code may need updates.
