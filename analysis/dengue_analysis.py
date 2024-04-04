import pandas as pd

from enums.dengue_columns import DengueColumns


class DengueAnalysis:
    def __init__(self, default_df: pd.DataFrame) -> None:
        self.df = default_df

    def clear_fields(): ...

    def rename_fields(self) -> list[str]:
        self.df.columns = [column_enum.value for column_enum in DengueColumns]

    def lesser_known_symptoms(self) -> None:
        symptoms_answers: pd.Series = (
            self.df[DengueColumns.SINTOMAS.value].str.split(", ").explode()
        )

        self.__get_lowest_occurrence_value(symptoms_answers)

    def relation_symptoms_media(self) -> None:
        # pegar a resposta da func lesser, porem precisa de ajustes.
        self.__get_relation_by_value(
            "Tosse",
            DengueColumns.SINTOMAS,
            DengueColumns.FONTE_INFORMACAO,
        )

    def relation_symptoms_schooling(self) -> None:
        # pegar a resposta da func lesser, porem precisa de ajustes.
        self.__get_relation_by_value(
            "Tosse",
            DengueColumns.SINTOMAS,
            DengueColumns.ESCOLARIDADE,
        )

    def lesser_know_combat(self) -> None:
        combat_answers: pd.Series = (
            self.df[DengueColumns.ACOES_COMBATE.value].str.split(",").explode()
        )

        self.__get_lowest_occurrence_value(combat_answers)

    def calculate_recidivism(self) -> None:
        recidivism_count = self.df[
            self.df[DengueColumns.QUANTIDADE_DENGUE.value].isin(
                ["Duas", "Três ou mais"]
            )
        ].shape[0]

        all_answers_count = self.df.shape[0]

        recidivism_hate = (recidivism_count / all_answers_count) * 100

        print(f"reincidência em :{recidivism_hate:.2f}%")

    def relation_recidivism_age(self) -> None:
        recidivism_values: list[str] = ["Duas", "Três ou mais"]

        for value in recidivism_values:
            print(f"Value:{value}\n==== idade\n")
            self.__get_relation_by_value(
                value,
                DengueColumns.QUANTIDADE_DENGUE,
                DengueColumns.IDADE,
            )
            print("==== gênero\n")
            self.__get_relation_by_value(
                value,
                DengueColumns.QUANTIDADE_DENGUE,
                DengueColumns.GENERO,
            )
            print("==== saneamento\n")
            self.__get_relation_by_value(
                value,
                DengueColumns.QUANTIDADE_DENGUE,
                DengueColumns.SANEAMENTO,
            )

    def relation_treatment_salary(self) -> None:
        salary_values: list[str] = (
            self.df[DengueColumns.RENDA.value].unique().tolist()
        )

        for salary in salary_values:
            print(f"Salario: {salary}\n")
            self.__get_relation_by_value(
                salary,
                DengueColumns.RENDA,
                DengueColumns.AVALIACAO_TRATAMENTO,
            )

    def relation_media_vaccine(self) -> None:
        vaccine_values: list[str] = (
            self.df[DengueColumns.VACINACAO_SUS.value].unique().tolist()
        )

        for value in vaccine_values:
            print(f"Decisão: {value}.\n")
            self.__get_relation_by_value(
                value,
                DengueColumns.VACINACAO_SUS,
                DengueColumns.FONTE_INFORMACAO,
            )

    def __get_relation_by_value(
        self,
        value: str,
        valueColumn: DengueColumns,
        relationColumn: DengueColumns,
        both: bool = False,
    ) -> None:
        group_by_value = self.df.groupby(
            self.df[valueColumn.value].str.contains(value)
        )
        if both:
            relation_by_value = group_by_value[
                relationColumn.value
            ].value_counts()

        relation_by_value = group_by_value.get_group(True)[
            relationColumn.value
        ].value_counts()

        print(f"{relation_by_value}\n")

    def __get_lowest_occurrence_value(self, answer_series: pd.Series) -> None:
        answer_count = answer_series.value_counts()
        print(answer_count)
        lowest_occurrence: int = answer_count.min()
        less_occurrence_values = answer_count[
            answer_count == lowest_occurrence
        ].index.tolist()
        print(f"{less_occurrence_values}\n")
