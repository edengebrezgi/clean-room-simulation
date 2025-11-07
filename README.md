# Clean-Room Data Simulation

This project demonstrates a privacy-safe workflow for comparing datasets from two different companies without exposing sensitive information. Using hashed emails, it identifies overlapping users while keeping personal data secure.

## Features

- Loads sample customer data for two companies
- Applies SHA-256 hashing to email addresses
- Drops raw emails to ensure privacy
- Performs an inner join to find overlapping users
- Saves hashed datasets and overlapping user table
- Displays a small sample of overlapping users in the console

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/clean-room-simulation.git
cd clean-room-simulation

