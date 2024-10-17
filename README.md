# Software Engineering Project

This repository contains the code for a software engineering course project. The project is built using Python and PostgreSQL, focusing on managing vending machine data.

## Table of Contents

- [Software Engineering Project](#software-engineering-project)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
  - [How to Use](#how-to-use)

## Introduction

This project aims to provide a system for managing vending machines and their products, including features like displaying vending machine details, product information, and user reviews. It serves as a practical exercise in applying software engineering principles.

## Features

- Vending machine management (list, details, stock)
- Product management (list, stock, details)
- Review and rating system for vending machines

## Technologies

- **Python 3.12.2**: Main programming language
- **PostgreSQL**: Database for storing application data
- **psycopg2**: Library for interacting with PostgreSQL

## Prerequisites

Make sure you have the following installed:

- Python 3.12.2
- PostgreSQL

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/falcaoanderson/Software-Engineering-Project.git
   cd software-engineering-project
   ```

2. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**
   - Create a PostgreSQL database named `vmdb`.
   - Run the SQL scripts located at `src/database/sql/builds.sql` and `src/database/sql/inserts.sql` to initialize the database schema and insert sample data.

4. **Configure environment variables:**
   - Create a `.env` file in the root directory with the following content:
     ```env
     DB_USER=your_database_user
     DB_PASSWORD=your_database_password
     ```

## How to Use

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Available commands and features:**
   - After running `main.py`, the application will provide a command-line interface for interacting with the vending machine system.
   - You can view vending machine details, check stock information and read reviews.