
# 📚 Python Scripts for Introduction to Electronics Filters

Welcome to the official repository of Python scripts accompanying the book and video course ** Introduction to Electronics Filters ** from [Tech Explorations](https://techexplorations.com). These scripts help you visualize and simulate the behaviour of first-order and second-order filters and perform other calculations related to basic electronic circuits.

This repository is designed to be a practical companion to your learning journey, enabling you to:

- Explore frequency responses of RC and RL filters.
- Conduct experiments and validate theoretical predictions.
- Automate calculations for cut-off frequencies, phase shifts, and time-domain responses.

---

## 📁 Repository Structure

```
.
├── /scripts/         # Contains Python scripts for simulations and analysis
├── /notebooks/       # Jupyter notebooks (optional - coming soon)
├── requirements.txt  # List of required Python packages
└── README.md         # This file
```

---

## ⚙️ Setting Up Your Local Python Environment

To run these scripts on your local machine, follow the steps below:

### 1️⃣ Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/futureshocked/introduction_to_electronics_filters.git
cd introduction_to_electronics_filters
```

### 2️⃣ Create a Virtual Environment

Creating a virtual environment is a best practice to avoid conflicts with other Python packages.

For **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

For **macOS / Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Required Packages

All required packages are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Scripts

Navigate to the `scripts/` directory and run any of the scripts:

```bash
cd scripts
python script_name.py
```

Replace `script_name.py` with the name of the script you want to run.

---

## 📝 Additional Notes

- **Jupyter Notebooks:** If you prefer running the code in an interactive environment, install Jupyter Notebook:

  ```bash
  pip install jupyter
  jupyter notebook
  ```

- **Python Version:** The scripts are compatible with **Python 3.9** and above.

- **Hardware Experiments:** The scripts complement hardware experiments described in the book/course. Even if you do not have the physical lab equipment, the simulations provide valuable insights.

---

## 📬 Contributing

If you find any issues or would like to contribute, feel free to open an **Issue** or submit a **Pull Request**!

---

## 📚 License

This project is licensed under the [MIT License](LICENSE).

---

### ✉️ Contact

For questions or feedback, please reach out via:

- **Website:** [https://www.techexplorations.com](https://www.techexplorations.com)

---

Happy experimenting and learning!
