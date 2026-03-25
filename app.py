from backend import create_app  # 폴더 이름이 backend라면 이렇게!

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)