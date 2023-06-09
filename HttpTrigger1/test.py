import logging

import azure.functions as func

def main(req: func.HttpRequest,outputblob:func.Out[str],inputblob:str,copyblob:func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # ファイルのバックアップ
    copytext = copyblob.set(inputblob)
    # 出力バインドしたファイルに変数の値を書き込みます
    outputtext = outputblob.set("テスト")

    return func.HttpResponse(f"{outputtext}")


