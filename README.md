# Restaurant Review Agent using RAG

This project implements an AI agent capable of processing and generating insights from restaurant reviews using Retrieval-Augmented Generation (RAG).

## 📚 Project Overview
The goal of this application is to analyze a collection of realistic restaurant reviews and use a sophisticated RAG pipeline to provide contextual and grounded answers to queries about restaurant sentiment, popular dishes, service quality, etc.

## 🚀 Getting Started

### Prerequisites
* Python 3.8+

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   The required packages are listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

### Running the Agent
The main logic resides in `main_file.py`. You can run the agent from your terminal:
```bash
python main_file.py
```

**Note:** The script relies on the `realistic_restaurant_reviews.csv` file for data source.

## 💾 Data Structure
The primary data source is `realistic_restaurant_reviews.csv`. This dataset contains structured and unstructured review data, including columns for:
*   `review_id`: Unique identifier for the review.
*   `rating`: Numerical star rating (e.g., 1 to 5).
*   `review_text`: The detailed text content of the review.
*   `date`: The date the review was posted.
*   (Other relevant columns based on the CSV structure)

## ✨ Architecture & Components
*   **`main_file.py`**: Entry point for the application. Initializes the RAG pipeline, processes the CSV data, and handles user interaction/querying.
*   **`vector.py`**: Handles the embedding generation and vector store operations, allowing semantic search over the review corpus.
*   **`requirements.txt`**: Lists all necessary Python packages (e.g., pandas, numpy, transformers, etc.).

## 💡 Usage Tips
*   **Querying:** When running the script, you will typically be prompted with a question to ask the agent. Ensure your query is specific to get the best results.
*   **Improvements:** For better performance or more complex logic, consider adding more advanced filtering or improving the prompt engineering within `main_file.py`.

