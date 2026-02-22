# Transaction-Processor

In this project, I refreshed my Python skills by practicing CSV handling and building a CLI tool to aggregate transaction data. 

## Features
- **CSV Aggregation:** Calculates total deposits and withdrawals per user.
- **Currency Conversion:** Automatically converts various currencies to a target currency using the [CurrencyAPI](https://currencyapi.com/).
- **Flexible Filtering:** Filter results by specific UIDs or transaction types (Deposit/Withdraw).
- **Customizable Output:** Supports custom delimiters and custom output filenames.
- **Caching:** API rates are cached locally during execution to minimize external requests.

## Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Melih7342/Transaction-Processor.git](https://github.com/Melih7342/Transaction-Processor.git)
   cd Transaction-Processor

 2. **Install dependencies:**
   ```bash
   pip install requests python-dotenv
```

 3. **Install dependencies:**

Create a .env file in the root directory and add your API key:
   ```bash
   API_KEY=your_currencyapi_key_here
```

## Usage

Run the tool via the command line. Example to filter for user 101 and convert everything to EUR:

```bash
python main.py -i transactions.csv -u 101 -c EUR -o summary_101.csv -v
```

### Arguments:

| Flag | Short | Description |
| :--- | :--- | :--- |
| `--input` | `-i` | **(Required)** Path to the input CSV file. |
| `--user` | `-u` | Filter by one or more UIDs (e.g., `-u 101 102`). |
| `--currency` | `-c` | Target currency for the summary (default: `USD`). |
| `--withdraw` | `-w` | Filter for withdrawals only. |
| `--deposit` | `-dp`| Filter for deposits only. |
| `--delimiter` | `-d` | Custom delimiter for output (default: `,`). |
| `--output` | `-o` | Provide a custom output filename (default: `summary.csv`). |
| `--verbose` | `-v` | Enable verbose mode for detailed processing logs. |

## Project Structure

- `main.py`: Entry point of the application that connects all modules.
- `argparsing.py`: Handles CLI arguments and file existence checks.
- `aggregate_logic.py`: Contains the core logic for processing and summing transaction data.
- `currencies.py`: Manages API requests and handles currency conversion rates.
- `write_summary.py`: Handles the CSV output and formatting of the results (2 decimal places).

## Example Commands

**Filter for specific users and convert to EUR:**
```bash
python main.py -i transactions.csv -u 101 102 -c EUR -v
```

**Show only withdrawals with a semicolon delimiter:**
```bash
python main.py -i data.csv -w -d ";" -o withdrawals_only.csv
```
