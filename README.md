# Artificial Intelligence Lab 

A collection of Python implementations covering **Inference, Deduction, Resolution Refutation, Answer Extraction, Probabilistic Reasoning, and Bayesian Networks**.

This repository contains the practical implementations for **Artificial Intelligence / Knowledge Representation Laboratory – Experiment 4**.

## 📚 Experiments

| No. | Experiment              | Concept                    |
| --- | ----------------------- | -------------------------- |
| 1   | Inference and Deduction | Forward Chaining           |
| 2   | Resolution Refutation   | Propositional Resolution   |
| 3   | Answer Extraction       | Knowledge Base Querying    |
| 4   | Probabilistic Reasoning | Bayes Theorem              |
| 5   | Belief Networks         | Bayesian Network Inference |

## 📂 Repository Structure

```text
Artificial_Intelligence_Lab_4/
│
├── Experiment_1_Forward_Chaining.py
├── Experiment_2_Resolution_Refutation.py
├── Experiment_3_Answer_Extraction.py
├── Experiment_4_Bayes_Theorem.py
├── Experiment_5_Bayesian_Network.py
│
└── README.md
```

## 🧠 Concepts Covered

### 1. Forward Chaining

Implements a simple rule-based inference engine that derives new facts from existing facts and rules.

**Concepts:**

* Facts
* Rules
* Premises
* Conclusions
* Forward chaining

### 2. Resolution Refutation

Implements propositional resolution to prove whether a query logically follows from a set of clauses.

**Concepts:**

* Logical clauses
* Complementary literals
* Resolvents
* Negation of query
* Empty clause
* Resolution refutation

### 3. Answer Extraction

Implements a simple knowledge-base querying system that extracts answers along with supporting evidence.

**Concepts:**

* Facts
* Predicates
* Rules
* Query answering
* Evidence-based reasoning

### 4. Bayes Theorem

Calculates posterior probability using prior probability, likelihood, and evidence.

**Formula:**

```text
P(H | E) = P(E | H) × P(H) / P(E)
```

The experiment demonstrates probabilistic reasoning using a diagnostic test example.

### 5. Bayesian Network

Constructs a small Bayesian network and performs probabilistic inference by enumeration.

Example network:

```text
Cloudy → Rain → WetGrass
```

The implementation calculates:

```text
P(Rain | WetGrass)
```

## 🛠️ Technologies Used

* **Python 3.9+**
* Python Standard Library
* Sets and tuples
* Functions
* Conditional statements
* Loops
* Probability calculations

No external libraries are required for the core experiments.

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/Soutikkk/Artificial_Intelligence_Lab_4.git
```

Navigate into the project:

```bash
cd Artificial_Intelligence_Lab_4
```

Run any experiment:

```bash
python Experiment_1_Forward_Chaining.py
```

or:

```bash
python Experiment_2_Resolution_Refutation.py
```

```bash
python Experiment_3_Answer_Extraction.py
```

```bash
python Experiment_4_Bayes_Theorem.py
```

```bash
python Experiment_5_Bayesian_Network.py
```

## 📊 Expected Results

The experiments demonstrate:

* Derivation of new facts using forward chaining
* Logical proof using resolution refutation
* Extraction of answers with supporting evidence
* Calculation of posterior probability using Bayes theorem
* Probabilistic inference using a Bayesian network

Example results include:

```text
Query proved: True
```

```text
P(Faulty | Positive) = 0.6667
Percentage = 66.67 %
```

```text
P(Rain | WetGrass) = 0.8182
Percentage = 81.82 %
```

## 🎯 Learning Outcomes

After completing these experiments, the following concepts can be understood and implemented:

* Rule-based inference
* Deductive reasoning
* Logical resolution
* Knowledge-base querying
* Explainable answer extraction
* Bayesian probabilistic reasoning
* Conditional probability
* Bayesian networks
* Probabilistic inference

## 👨‍💻 Author

**Soutik Mandal**

Artificial Intelligence / Machine Learning Student

GitHub: [Soutikkk](https://github.com/Soutikkk)

---

⭐ If you find this repository useful, consider giving it a star!
