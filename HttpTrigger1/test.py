import logging

import azure.functions as func

def main(req: func.HttpRequest,outputblob:func.Out[str],inputblob:func.InputStream[str],copyblob:func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # ファイルのバックアップ
    copyblob.set(inputblob)
    # 出力バインドしたファイルに変数の値を書き込みます
    outputtext = outputblob.set("テスト")

    return func.HttpResponse(f"{outputtext}")


