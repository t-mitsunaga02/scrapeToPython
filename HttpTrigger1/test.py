import os

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # ファイルの作成先のパスを指定
    file_path = os.path.join(os.getcwd(), "example.txt")

    # ファイルに書き込むデータを指定
    file_data = "Hello, Azure Functions!"

    # ファイルを書き込みモードで開き、データを書き込む
    with open(file_path, "w") as file:
        file.write(file_data)

    # レスポンスメッセージを作成
    response = func.HttpResponse(
        f"ファイルを作成しました: {file_path}",
        status_code=200
    )

    return response


