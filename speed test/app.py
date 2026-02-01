from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import time, os
app = Flask(__name__)

# CORS setup taaki speed test block na ho
CORS(app, resources={r"/*": {"origins": "*"}})

# 1. Main Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Download speed test (random data stream)
@app.route('/download-test')
def download_test():
    def generate():
        chunk = os.urandom(1024 * 64)  # 64KB
        for _ in range(800):  # ~50MB total
            yield chunk
    return app.response_class(generate(), mimetype='application/octet-stream')


# Upload speed test (data receive karke time measure hoga)
@app.route('/upload-test', methods=['POST'])
def upload_test():
    start = time.time()
    _ = request.get_data()
    end = time.time()
    return jsonify({
        "time": round(end - start, 2)
    })


# 2. Logo Route (Templates folder se image uthane ke liye)
@app.route('/speedtest-logo.png')
def get_logo():
    return send_from_directory('templates', 'speedtest-logo.png')

# 3. Google Console Verification
@app.route('/google4cf6c04200746e22.html')
def google_verify():
    return render_template('google4cf6c04200746e22.html')

# 4. Upload Speed Test Endpoint
@app.route('/upload-test', methods=['POST', 'OPTIONS'])
def upload_test():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "ok"})

# 5. Extra Pages (SEO aur AdSense ke liye)
@app.route('/privacy')
def privacy(): 
    return render_template('privacy.html')

@app.route('/contact')
def contact(): 
    return render_template('contact.html')

@app.route('/terms')
def terms(): 
    return render_template('terms.html')

if __name__ == '__main__':
    # Local machine par run karne ke liye

    app.run(debug=True, port=8000, host='127.0.0.1')
