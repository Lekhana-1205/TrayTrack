# Path: src/config/supabase_client.py
# Purpose: Connect to Supabase using URL and API Key from .env

import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load local .env file (for local development)
load_dotenv()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "Supabase URL or Key not found! "
        "Make sure you set them in Streamlit Secrets or your .env file."
    )

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
