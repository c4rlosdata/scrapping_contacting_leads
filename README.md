# Business Directory Scraper and WhatsApp Messaging Automation

This project automates two main tasks for lead generation and client outreach:
1. **Scraping Contact Information**: Extracts phone numbers from a commercial directory website.
2. **Automated WhatsApp Messaging**: Uses the scraped contact data to send personalized messages via WhatsApp.

The project can be customized to target specific sectors and scales well for outreach campaigns by sending automated messages to a large number of prospects.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [File Structure](#file-structure)
8. [Troubleshooting](#troubleshooting)
9. [Future Enhancements](#future-enhancements)
10. [License](#license)

---

## Project Overview
The project is designed to help businesses:
- Find contact information from relevant companies in a commercial directory.
- Automate sending introductory messages to potential clients over WhatsApp, with a customizable message template.

## Features
- **Web Scraping**: Automatically scrapes contact numbers from a specified directory based on sector keywords.
- **Data Export**: Saves contact data in an Excel file for review and reuse.
- **Automated WhatsApp Messaging**: Sends personalized messages to each contact using the WhatsApp Web platform.
- **Customization**: Includes a customizable message template for personalized outreach.

## Requirements
- Python 3.8+
- Libraries:
  - `requests` (for HTTP requests)
  - `BeautifulSoup` (for HTML parsing and web scraping)
  - `pandas` (for data handling and Excel export)
  - `pywhatkit` (for sending WhatsApp messages)
  - `time` (for managing request intervals)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/directory-whatsapp-scraper.git
   cd directory-whatsapp-scraper
   ```
2. Install the required libraries as listed above.

## Configuration
1. **Directory URL**:
   - The base URL for the directory is specified in `buscar_telefones_guia_mais`.
   - Update `setor` to target a specific industry (e.g., `alimentos` for food).
   
2. **WhatsApp Message Template**:
   - The message template is defined in the `mensagem_template` variable. Customize it to fit your outreach campaign.
   - You can personalize it by adding placeholders for dynamic text, if necessary.

3. **Excel File**:
   - The scraped contact numbers will be saved in `celulares_python.xlsx`. This file is used by the WhatsApp messaging script.

## Usage
### Step 1: Run the Scraper
Run the script to scrape phone numbers from the specified directory:
```bash
python scrape_contacts.py
```
This will generate an Excel file, `celulares_python.xlsx`, containing the extracted phone numbers.

### Step 2: Send WhatsApp Messages
Use the following command to send automated messages to the scraped contacts:
```bash
python send_messages.py
```

Each contact will receive a message via WhatsApp, with a short delay between messages to avoid issues with spam detection.

## File Structure
```
├── scrape_contacts.py         # Script for scraping contact numbers
├── send_messages.py           # Script for sending WhatsApp messages
├── celulares_python.xlsx      # Output file containing scraped phone numbers
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Troubleshooting
- **WhatsApp Web Authentication**: Ensure WhatsApp Web is open and you’re logged in when running the `send_messages.py` script.
- **Scraping Delays**: The script includes delays to prevent server blocks. Adjust these if you encounter rate-limiting issues.
- **Message Formatting Errors**: Ensure the message template does not exceed WhatsApp’s character limit and follows WhatsApp's guidelines.

## Future Enhancements
- **Dynamic Message Personalization**: Include custom variables for dynamic message content.
- **Error Logging**: Add error logging for failed message deliveries or failed scraping attempts.
- **Rate Control**: Add configurable delays between message sends for different campaign types.

## License
This project is licensed under the MIT License.
