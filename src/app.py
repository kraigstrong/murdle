from openai import OpenAI
import os


def get_openai_api_key():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API_KEY environment variable is not set.")
    return api_key

def main():
    client = OpenAI(
        # This is the default and can be omitted
        api_key=get_openai_api_key()
    )

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=50,
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant"
            }, 
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        
    )
    print(chat_completion)

if __name__ == "__main__":
    # This block ensures that the main function is executed when the script is run
    main()