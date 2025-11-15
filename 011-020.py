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
    return df_customer, df_receipt, df_store


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 演習問題
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-011: 顧客データ（df_customer）から顧客ID（customer_id）の末尾が1のものだけ全項目抽出し、10件表示せよ。
    """)
    return


@app.cell
def _(df_customer, pl):
    df_customer.filter(pl.col("customer_id").str.ends_with("1")).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-012: 店舗データ（df_store）から、住所 (address) に"横浜市"が含まれるものだけ全項目表示せよ。
    """)
    return


@app.cell
def _(df_store, pl):
    df_store.filter(pl.col("address").str.contains("横浜市"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-013: 顧客データ（df_customer）から、ステータスコード（status_cd）の先頭がアルファベットのA〜Fで始まるデータを全項目抽出し、10件表示せよ。
    """)
    return


@app.cell
def _(df_customer, pl):
    df_customer.filter(pl.col("status_cd").str.contains(r"^[A-F]")).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-014: 顧客データ（df_customer）から、ステータスコード（status_cd）の末尾が数字の1〜9で終わるデータを全項目抽出し、10件表示せよ。
    """)
    return


@app.cell
def _(df_customer, pl):
    df_customer.filter(pl.col("status_cd").str.contains(r"[1-9]$")).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-015: 顧客データ（df_customer）から、ステータスコード（status_cd）の先頭がアルファベットのA〜Fで始まり、末尾が数字の1〜9で終わるデータを全項目抽出し、10件表示せよ。
    """)
    return


@app.cell
def _(df_customer, pl):
    df_customer.filter(pl.col("status_cd").str.contains(r"^[A-F].*[1-9]$")).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-016: 店舗データ（df_store）から、電話番号（tel_no）が3桁-3桁-4桁のデータを全項目表示せよ。
    """)
    return


@app.cell
def _(df_store, pl):
    df_store.filter(pl.col("tel_no").str.contains(r"^\d{3}-\d{3}-\d{4}$"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-017: 顧客データ（df_customer）を生年月日（birth_day）で高齢順にソートし、先頭から全項目を10件表示せよ。
    """)
    return


@app.cell
def _(df_customer):
    df_customer.sort(by="birth_day").head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-018: 顧客データ（df_customer）を生年月日（birth_day）で若い順にソートし、先頭から全項目を10件表示せよ。
    """)
    return


@app.cell
def _(df_customer):
    df_customer.sort(by="birth_day", descending=True).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-019: レシート明細データ（df_receipt）に対し、1件あたりの売上金額（amount）が高い順にランクを付与し、先頭から10件表示せよ。項目は顧客ID（customer_id）、売上金額（amount）、付与したランクを表示させること。なお、売上金額（amount）が等しい場合は同一順位を付与するものとする。
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["customer_id", "amount"]].with_columns(
        pl.col("amount").rank(method="min", descending=True).alias("amount_rank")
    ).sort(by="amount_rank").head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    P-020: レシート明細データ（df_receipt）に対し、1件あたりの売上金額（amount）が高い順にランクを付与し、先頭から10件表示せよ。項目は顧客ID（customer_id）、売上金額（amount）、付与したランクを表示させること。なお、売上金額（amount）が等しい場合でも別順位を付与すること。
    """)
    return


@app.cell
def _(df_receipt, pl):
    df_receipt[["customer_id", "amount"]].sort(
        by="amount", descending=True
    ).with_columns(pl.arange(1, pl.len() + 1).alias("amount_rank")).sort(
        by="amount_rank"
    ).head(10)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
