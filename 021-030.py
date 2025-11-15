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
    return (df_receipt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 演習問題
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-021: レシート明細データ（df_receipt）に対し、件数をカウントせよ。
    """)
    return


@app.cell
def _(df_receipt):
    len(df_receipt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-022: レシート明細データ（df_receipt）の顧客ID（customer_id）に対し、ユニーク件数をカウントせよ。
    """)
    return


@app.cell
def _(df_receipt):
    len(df_receipt.unique("customer_id"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-023: レシート明細データ（df_receipt）に対し、店舗コード（store_cd）ごとに売上金額（amount）と売上数量（quantity）を合計せよ。
    """)
    return


@app.cell
def _(df_receipt):
    df_receipt[["store_cd", "amount", "quantity"]].group_by(
        "store_cd", maintain_order=True
    ).sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-024: レシート明細データ（df_receipt）に対し、顧客ID（customer_id）ごとに最も新しい売上年月日（sales_ymd）を求め、10件表示せよ。
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["customer_id", "sales_ymd"]].group_by("customer_id").agg(
        pl.col("sales_ymd").max().alias("latest_sales_ymd")
    ).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-025: レシート明細データ（df_receipt）に対し、顧客ID（customer_id）ごとに最も古い売上年月日（sales_ymd）を求め、10件表示せよ。
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["customer_id", "sales_ymd"]].group_by("customer_id").agg(
        pl.col("sales_ymd").min().alias("oldest_sales_ymd")
    ).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-026: レシート明細データ（df_receipt）に対し、顧客ID（customer_id）ごとに最も新しい売上年月日（sales_ymd）と古い売上年月日を求め、両者が異なるデータを10件表示せよ。
    """)
    return


@app.cell
def _(df_receipt, pl):
    # 最新売上と最古売上のカラムを追加
    df_026 = (
        df_receipt[["customer_id", "sales_ymd"]]
        .group_by("customer_id")
        .agg(
            [
                pl.col("sales_ymd").max().alias("latest_sales_ymd"),
                pl.col("sales_ymd").min().alias("oldest_sales_ymd"),
            ]
        )
    )
    # 両者の異なる行のみ抽出
    df_026.filter(pl.col("latest_sales_ymd") != pl.col("oldest_sales_ymd")).head(10)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-027: レシート明細データ（df_receipt）に対し、店舗コード（store_cd）ごとに売上金額（amount）の平均を計算し、降順でTOP5を表示せよ。
    """)
    return


@app.cell
def _(df_receipt):
    df_receipt[["store_cd", "amount"]].group_by("store_cd").mean().sort(
        "amount", descending=True
    ).head(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-028: レシート明細データ（df_receipt）に対し、店舗コード（store_cd）ごとに売上金額（amount）の中央値を計算し、降順でTOP5を表示せよ。
    """)
    return


@app.cell
def _(df_receipt):
    df_receipt[["store_cd", "amount"]].group_by("store_cd").median().sort(
        "amount", descending=True
    ).head(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-029: レシート明細データ（df_receipt）に対し、店舗コード（store_cd）ごとに商品コード（product_cd）の最頻値を求め、10件表示させよ。
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["store_cd", "product_cd"]].group_by("store_cd").agg(
        pl.col("product_cd").mode()
    ).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-030: レシート明細データ（df_receipt）に対し、店舗コード（store_cd）ごとに売上金額（amount）の分散を計算し、降順で5件表示せよ。
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["store_cd", "amount"]].group_by("store_cd").agg(
        pl.col("amount").var(ddof=0).alias("amount_var")
    ).sort("amount_var", descending=True).head(5)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
