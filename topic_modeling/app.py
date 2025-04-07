from service import extract_topic_from_text
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/predict/topic', methods=['POST'])
def get_topic():
  try:
      data = request.get_json()
      if "text" not in data:
          return jsonify({"error": "Missing 'text' field"}), 400
      result = extract_topic_from_text(data["text"])
      return jsonify({"Text topic": result}), 201
  except Exception as e:
      return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
