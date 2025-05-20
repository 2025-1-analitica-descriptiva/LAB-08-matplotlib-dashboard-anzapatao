# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os


def load_data():
    """
    Carga los datos desde el archivo CSV y devuelve un DataFrame de pandas.
    """
    # Cargar los datos desde el archivo CSV
    df = pd.read_csv("files/input/shipping-data.csv")
    return df


def create_visual_for_shipping_wherehouse(df):
    df = df.copy()
    plt.figure()
    counts = df["Warehouse_block"].value_counts()
    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Wherehouse block",
        ylabel="Record count",
        color="tab:blue",
        fontsize=8,
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    # crear docs si no existe
    if not os.path.exists("docs"):
        os.makedirs("docs")
    plt.savefig("docs/shipping_per_warehouse.png")
    # return counts


def create_visual_for_mode_of_shipment(df):
    df = df.copy()
    plt.figure()
    counts = df["Mode_of_Shipment"].value_counts()
    counts.plot.pie(
        title="Mode of Shipment",
        wedgeprops={"width": 0.35},
        xlabel="Mode of Shipment",
        ylabel="",
        color=["tab:blue", "tab:orange", "tab:green", "tab:red"],
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    # crear docs si no existe
    if not os.path.exists("docs"):
        os.makedirs("docs")
    plt.savefig("docs/mode_of_shipment.png")
    # return counts


def create_visual_average_custumer_rating(df):
    df = df.copy()
    plt.figure()
    df = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )
    df.columns = df.columns.droplevel(0)
    df = df[["mean","min","max"]]
    plt.barh(
        y=df.index.values,
        width = df['max'].values - 1,
        left = df['min'].values,
        height = 0.9,
        color = "lightgray",
        alpha = 0.8,
    )
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
    ]
    plt.barh(
        y=df.index.values,
        width=df["mean"].values,
        left=df["min"].values,
        height=0.5,
        color=colors,
        alpha=1.0,
    )
    plt.title("Average Customer Rating")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.savefig("docs/average_customer_rating.png")
    return df

def create_visual_for_weight_distribution(df):
    df = df.copy()
    plt.figure()
    df["Weight_in_gms"].plot.hist(
        title="Shipped Weight Distribution",
        color="tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    # crear docs si no existe
    if not os.path.exists("docs"):
        os.makedirs("docs")
    plt.savefig("docs/weight_distribution.png")
    # return counts

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    df = load_data()
    create_visual_for_shipping_wherehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_average_custumer_rating(df)
    create_visual_for_weight_distribution(df)

if __name__ == "__main__":
    # Llamar a la función para generar el dashboard
    pregunta_01()
