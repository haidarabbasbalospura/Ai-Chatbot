# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# # Initialize the Gemini model
# llm = ChatGoogleGenerativeAI(
#     model="gemini-pro",
#     google_api_key=os.getenv("GOOGLE_API_KEY"),
#     temperature=0.7
# )

# # Initialize conversation memory
# memory = ConversationBufferMemory()

# # Create conversation chain
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory,
#     verbose=True
# )

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         data = request.json
#         user_message = data.get('message')
        
#         if not user_message:
#             return jsonify({'error': 'No message provided'}), 400

#         # Get response from the model
#         response = conversation.predict(input=user_message)
        
#         return jsonify({'response': response})

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return jsonify({'error': 'An error occurred processing your request'}), 500

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_together import Together
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# class ModelManager:
#     def __init__(self):
#         self.current_model = None
#         self.memory = ConversationBufferMemory()
#         self.conversation = None
#         self.settings = {
#             'provider': 'google',
#             'model': 'gemini-pro',
#             'temperature': 0.7
#         }
    
#     def initialize_model(self, provider, model_name, api_key, temperature=0.7):
#         try:
#             if provider == 'google':
#                 self.current_model = ChatGoogleGenerativeAI(
#                     model=model_name,
#                     google_api_key=api_key,
#                     temperature=temperature
#                 )
#             elif provider == 'together':
#                 os.environ['TOGETHER_API_KEY'] = api_key
#                 self.current_model = Together(
#                     model=model_name,
#                     temperature=temperature
#                 )
            
#             self.conversation = ConversationChain(
#                 llm=self.current_model,
#                 memory=self.memory,
#                 verbose=True
#             )
            
#             return True
#         except Exception as e:
#             print(f"Error initializing model: {str(e)}")
#             return False

# model_manager = ModelManager()

# @app.route('/update-settings', methods=['POST'])
# def update_settings():
#     try:
#         data = request.json
#         success = model_manager.initialize_model(
#             provider=data['provider'],
#             model_name=data['model'],
#             api_key=data['apiKey'],
#             temperature=float(data['temperature'])
#         )
        
#         if success:
#             return jsonify({'success': True})
#         else:
#             return jsonify({'success': False, 'error': 'Failed to initialize model'})
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)})

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         if not model_manager.conversation:
#             # Initialize with default settings if not already initialized
#             model_manager.initialize_model(
#                 provider='google',
#                 model_name='gemini-pro',
#                 api_key=os.getenv('GOOGLE_API_KEY'),
#                 temperature=0.7
#             )
        
#         data = request.json
#         user_message = data.get('message')
        
#         if not user_message:
#             return jsonify({'error': 'No message provided'}), 400

#         response = model_manager.conversation.predict(input=user_message)
#         return jsonify({'response': response})

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return jsonify({'error': 'An error occurred processing your request'}), 500

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_together import Together
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

class ModelManager:
    def __init__(self):
        self.current_model = None
        self.memory = ConversationBufferMemory()
        self.conversation = None
        self.settings = {
            'provider': 'google',
            'model': 'gemini-pro',
            'temperature': 0.7
        }
    
    def initialize_model(self, provider, model_name, temperature=0.7):
        try:
            if provider == 'google':
                self.current_model = ChatGoogleGenerativeAI(
                    model=model_name,
                    temperature=temperature
                )
            elif provider == 'together':
                self.current_model = Together(
                    model=model_name,
                    temperature=temperature
                )
            
            self.conversation = ConversationChain(
                llm=self.current_model,
                memory=self.memory,
                verbose=True
            )
            
            return True
        except Exception as e:
            print(f"Error initializing model: {str(e)}")
            return False

model_manager = ModelManager()

@app.route('/update-settings', methods=['POST'])
def update_settings():
    try:
        data = request.json
        success = model_manager.initialize_model(
            provider=data['provider'],
            model_name=data['model'],
            temperature=float(data['temperature'])
        )
        
        if success:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Failed to initialize model'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        if not model_manager.conversation:
            # Initialize with default settings if not already initialized
            model_manager.initialize_model(
                provider='google',
                model_name='gemini-pro',
                temperature=0.7
            )
        
        data = request.json
        print("data", data)
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        response = model_manager.conversation.predict(input=user_message)
        return jsonify({'response': response})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An error occurred processing your request'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)