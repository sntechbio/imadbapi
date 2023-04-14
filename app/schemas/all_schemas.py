from pydantic import BaseModel, Field
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


class CytokinesCovid(BaseModel):
    id: Optional[int] = Field(None, description='ID', gt=0)
    patient_information_id: Optional[int] = Field(None, description='Patient Information ID', gt=0)
    FGF_basic: Optional[float] = Field(None, description='FGF Basic')
    G_CSF: Optional[float] = Field(None, description='G-CSF')
    GM_CSF: Optional[float] = Field(None, description='GM-CSF')
    PDGF: Optional[float] = Field(None, description='PDGF')
    VEGF: Optional[float] = Field(None, description='VEGF')
    IL_1_beta: Optional[float] = Field(None, description='IL-1 beta')
    IL_6: Optional[float] = Field(None, description='IL-6')
    IL_12p70: Optional[float] = Field(None, description='IL-12p70')
    IFN_gamma: Optional[float] = Field(None, description='IFN gamma')
    TNF_alpha: Optional[float] = Field(None, description='TNF alpha')
    CCL2: Optional[float] = Field(None, description='CCL2')
    CCL3: Optional[float] = Field(None, description='CCL3')
    CCL4: Optional[float] = Field(None, description='CCL4')
    CCL5: Optional[float] = Field(None, description='CCL5')
    Eotaxin: Optional[float] = Field(None, description='Eotaxin')
    IL_4: Optional[float] = Field(None, description='IL-4')
    IL_5: Optional[float] = Field(None, description='IL-5')
    IL_13: Optional[float] = Field(None, description='IL-13')
    IL_2: Optional[float] = Field(None, description='IL-2')
    IL_10: Optional[float] = Field(None, description='IL-10')
    CXCL10: Optional[float] = Field(None, description='CXCL10')
    CXCL8: Optional[float] = Field(None, description='CXCL8')
    IL_1ra: Optional[float] = Field(None, description='IL-1ra')
    IL_7: Optional[float] = Field(None, description='IL-7')
    IL_9: Optional[float] = Field(None, description='IL-9')
    IL_15: Optional[float] = Field(None, description='IL-15')
    IL_17: Optional[float] = Field(None, description='IL-17')
    DIS: Optional[int] = Field(None, description='DIS', ge=0)

    class Config:
        orm_mode = True
