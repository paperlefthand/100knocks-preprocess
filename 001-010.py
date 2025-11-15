import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # データサイエンス100本ノック（構造化データ加工編） - Python
    """)
    return


@app.cell
def _():
    import polars as pl

    return (pl,)


@app.cell
def _():
    import sys

    sys.path.append("common")
    from loader import load_data

    df_category, df_customer, df_geocode, df_product, df_receipt, df_store = load_data()
    return df_receipt, df_store


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 演習問題
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-001: レシート明細データ（df_receipt）から全項目の先頭10件を表示し、どのようなデータを保有しているか目視で確認せよ。
    """)
    return


@app.cell
def _(df_receipt):
    df_receipt.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-002: レシート明細データ（df_receipt）から売上年月日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上金額（amount）の順に列を指定し、10件表示せよ。
    """)
    return


@app.cell
def _(df_receipt):
    df_receipt[["sales_ymd", "customer_id", "product_cd", "amount"]].head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-003: レシート明細データ（df_receipt）から売上年月日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上金額（amount）の順に列を指定し、10件表示せよ。ただし、sales_ymdsales_dateに項目名を変更しながら抽出すること。
    """)
    return


@app.cell
def _(df_receipt):
    df_receipt[["sales_ymd", "customer_id", "product_cd", "amount"]].rename(
        {"sales_ymd": "sales_date"}
    ).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-004: レシート明細データ（df_receipt）から売上日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上金額（amount）の順に列を指定し、以下の条件を満たすデータを抽出せよ。
    - 顧客ID（customer_id）が"CS018205000001"
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["sales_ymd", "customer_id", "product_cd", "amount"]].filter(
        pl.col("customer_id") == "CS018205000001"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-005: レシート明細データ（df_receipt）から売上日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上金額（amount）の順に列を指定し、以下の全ての条件を満たすデータを抽出せよ。
    - 顧客ID（customer_id）が"CS018205000001"
    - 売上金額（amount）が1,000以上
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["sales_ymd", "customer_id", "product_cd", "amount"]].filter(
        (pl.col("customer_id") == "CS018205000001") & (pl.col("amount") >= 1000)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-006: レシート明細データ（df_receipt）から売上日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上数量（quantity）、売上金額（amount）の順に列を指定し、以下の全ての条件を満たすデータを抽出せよ。
    - 顧客ID（customer_id）が"CS018205000001"
    - 売上金額（amount）が1,000以上または売上数量（quantity）が5以上
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["sales_ymd", "customer_id", "product_cd", "quantity", "amount"]].filter(
        (pl.col("customer_id") == "CS018205000001")
        & ((pl.col("amount") >= 1000) | (pl.col("quantity") >= 5))
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-007: レシート明細データ（df_receipt）から売上日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上金額（amount）の順に列を指定し、以下の全ての条件を満たすデータを抽出せよ。
    - 顧客ID（customer_id）が"CS018205000001"
    - 売上金額（amount）が1,000以上2,000以下
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["sales_ymd", "customer_id", "product_cd", "amount"]].filter(
        (pl.col("customer_id") == "CS018205000001")
        & (pl.col("amount") >= 1000)
        & (pl.col("amount") <= 2000)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-008: レシート明細データ（df_receipt）から売上日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上金額（amount）の順に列を指定し、以下の全ての条件を満たすデータを抽出せよ。
    - 顧客ID（customer_id）が"CS018205000001"
    - 商品コード（product_cd）が"P071401019"以外
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["sales_ymd", "customer_id", "product_cd", "amount"]].filter(
        (pl.col("customer_id") == "CS018205000001")
        & (pl.col("product_cd") != "P071401019")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-009: 以下の処理において、出力結果を変えずにORをANDに書き換えよ。
    `df_store.query('not(prefecture_cd == "13" | floor_area > 900)')`
    """)
    return


@app.cell
def _(df_store, pl):
    df_1 = df_store.filter(
        ~((pl.col("prefecture_cd") == 13) | (pl.col("floor_area") > 900))
    )
    df_2 = df_store.filter(
        (pl.col("prefecture_cd") != 13) & (pl.col("floor_area") <= 900)
    )
    df_1.equals(df_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-010: 店舗データ（df_store）から、店舗コード（store_cd）が"S14"で始まるものだけ全項目抽出し、10件表示せよ。
    """)
    return


@app.cell
def _(df_store, pl):
    df_store.filter(pl.col("store_cd").str.starts_with("S14")).head(10)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
