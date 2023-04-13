from pydantic import BaseModel
from typing import Optional, Text


class AgeGroup(BaseModel):
    id: Optional[int]
    group: Optional[str]

    class Config:
        orm_mode = True


class PatientInformationCvd(BaseModel):
    id: int
    age: Optional[int]
    sex: Optional[str]
    profession: Optional[str]
    schooling: Optional[str]
    address: Optional[str]
    income: Optional[str]
    marital_status: Optional[str]
    imc: Optional[float]
    group: Optional[str]
    vaccination: Optional[str]

    class Config:
        orm_mode = True


class NutricionalData(BaseModel):
    id: Optional[int]
    nutricional_group: Optional[str]

    class Config:
        orm_mode = True


class FrequencyFoodConsumption(BaseModel):
    id: Optional[int]
    frequency: Optional[str]

    class Config:
        orm_mode = True


class FoodConsumption(BaseModel):
    id: Optional[int]
    patient_information_id: Optional[int]
    age_group_id: Optional[int]
    ethnicity_id: Optional[int]
    nutritional_data_id: Optional[int]
    carga_viral: Optional[float]
    comorbity: Optional[Text]
    leite: Optional[int]
    Iogurte: Optional[int]
    queijo_branco: Optional[int]
    queijo_amarelo: Optional[int]
    requeijao: Optional[int]
    ovo_frito: Optional[int]
    ovo_cozido: Optional[int]
    carne_de_boi: Optional[int]
    carne_de_porco: Optional[int]
    frango: Optional[int]
    peixe_fresco: Optional[int]
    peixe_enlatado: Optional[int]
    carne_conservada_no_sal: Optional[int]
    visceras: Optional[int]
    azeite: Optional[int]
    bacon_toucinho_banha_de_porco: Optional[int]
    arroz_integral: Optional[int]
    arroz_polido: Optional[int]
    pao_integral: Optional[int]
    pao_frances: Optional[int]
    bolo_caseiro: Optional[int]
    macarrao: Optional[int]
    feijao: Optional[int]
    lentilhas: Optional[int]
    folha_crua: Optional[int]
    folha_refogada_cozida: Optional[int]
    legumes_cozidos: Optional[int]
    tuberculos: Optional[int]
    frutas: Optional[int]
    sucos_naturais_sem_acucar: Optional[int]
    suco_natural_com_acucar: Optional[int]
    tortas_e_doces: Optional[int]
    cafe_com_acucar: Optional[int]
    refrigerante: Optional[int]
    suco_artificial_com_acucar: Optional[int]
    adocante: Optional[int]
    embutidos: Optional[int]
    molhos_para_salada: Optional[int]
    manteiga_margarina_maionese: Optional[int]
    snacks: Optional[int]
    petiscos: Optional[int]
    enlatados: Optional[int]
    pao_de_forma: Optional[int]
    biscoito_salgado: Optional[int]
    biscoito_doce: Optional[int]
    bolo_industrializado: Optional[int]
    Sorvetes_balas_guloseimas: Optional[int]
    geleia_industrializadas: Optional[int]
    chocolate_s_achocolatados: Optional[int]
    macarrao_instantaneo: Optional[int]

    class Config:
        orm_mode = True
