# JSONtoCSV

JSONtoCSV is a collection of simple Python scripts that convert a JSON file to a CSV file. These scripts are particularly useful for dealing with large JSON files that need to be processed and analyzed in a more user-friendly format.

There are two scripts available in this project:

1. `json_to_csv.py`: A basic script that converts JSON data with a fixed structure to a CSV file.
2. `adv_json_to_csv.py`: An advanced script that allows you to dynamically specify the fields you want to extract from the JSON data via command-line arguments.

## Prerequisites

- Python 3.x installed on your system.

## Usage

### Basic JSON to CSV Conversion (`json_to_csv.py`)

1. Clone this repository or download the `json_to_csv.py` script to your local machine.
2. Open a command prompt or terminal window and navigate to the directory containing the `json_to_csv.py` script.
3. Run the script with the following command, providing the input JSON file and output CSV file paths as arguments:

```bash
python json_to_csv.py /path/to/your/input.json /path/to/your/output.csv
```
Replace `/path/to/your/input.json` with the actual path to your JSON file, and `/path/to/your/output.csv` with the desired path for the output CSV file.

### Advanced JSON to CSV Conversion (`adv_json_to_csv.py`)

1. Clone this repository or download the `adv_json_to_csv.py` script to your local machine.
2. Open a command prompt or terminal window and navigate to the directory containing the `adv_json_to_csv.py` script.
3. Run the script with the following command, providing the input JSON file, output CSV file paths, and field names as arguments:

```bash
python adv_json_to_csv.py /path/to/your/input.json /path/to/your/output.csv title description slug.current id
```

Replace `/path/to/your/input.json` with the actual path to your JSON file, and `/path/to/your/output.csv` with the desired path for the output CSV file. Also, replace `title description slug.current id` with the field names you want to extract from the JSON file.

## Example JSON Structure

The input JSON file should contain an array of objects with the following structure:

```json
{
  "result": [
    {
      "title": "Example Title",
      "description": "Example Description",
      "slug": {
        "current": "/example/slug"
      },
      "id": "example-id"
    },
    ...
  ]
}
```
The scripts will extract the data from the `result` array and convert it into a CSV format with columns for "title", "description", "slug", and "id".

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit pull requests for improvements, bug fixes, or new features.

## Support

If you encounter any issues or have questions, please open a GitHub issue, and we'll do our best to help you.
