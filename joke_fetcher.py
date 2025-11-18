#!/usr/bin/env python3
"""
Simple script to fetch a random joke from an API and display it.
"""

import requests
import json


def fetch_joke():
    """Fetch a random joke from the JokeAPI."""
    try:
        # Using JokeAPI - a free joke API
        url = "https://official-joke-api.appspot.com/random_joke"
        
        print("Fetching a joke...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        joke_data = response.json()
        
        # Display the joke
        print("\n" + "="*50)
        print("HERE'S YOUR JOKE:")
        print("="*50)
        print(f"\n{joke_data['setup']}")
        print(f"\n{joke_data['punchline']}")
        print("\n" + "="*50 + "\n")
        
        return joke_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error parsing joke data: {e}")
        return None


if __name__ == "__main__":
    print("🎭 Welcome to the Joke Fetcher! 🎭\n")
    fetch_joke()
