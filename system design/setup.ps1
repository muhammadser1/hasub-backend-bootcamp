# Define the path to the virtual environment directory
$venvPath = ".\venv"

# Check if the virtual environment directory exists
if (-Not (Test-Path $venvPath)) {
    # Create the virtual environment if it does not exist
    python -m venv $venvPath
}

# Activate the virtual environment
& "$venvPath\Scripts\Activate.ps1"

# Install dependencies from requirements.txt
pip install -r requirements.txt

Write-Host "Dependencies installed successfully in the virtual environment."

python Conway_Game_of_Life
