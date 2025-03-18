from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)


# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    return jsonify({
        "response": "Hello, I am a chatbot!"
    })

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy"
    })

# Start app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)



# async def invoke_agent(self, text: str):

#     # Add the human message and and get the token generator
#     token_generator = self.agent_chat_stream.add_human_message_and_invoke(text)

#     # Iterate through the token generator
#     sentence_index = 0 # To get last audio index
#     for sentence in sentence_stream(token_generator):

#         print("Sentence:", sentence)

#         # create audio from text the and send
#         asyncio.create_task(self.tts_and_send(sentence, sentence_index))

#         sentence_index += 1

#     # Last sentence processed. Send the last audio index
#     await self.websocket.send(json.dumps({
#         "type": "last_audio_index",
#         "index": sentence_index - 1  # -1 because we incremented before exiting the loop
#     }))

#     # Start listening again
#     self.start_listening()
