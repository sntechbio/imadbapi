from sqlalchemy import Column, Integer, String, Float, Text
from app.config.database import Base


class AgeGroup(Base):
    __tablename__ = "age_group"

    id = Column(Integer, primary_key=True, index=True)
    group = Column(String(60), index=True)


class PatientInformationCvd(Base):
    __tablename__ = "patient_information_cvd"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, index=True)
    sex = Column(String(10), index=True)
    profession = Column(String(60), index=True)
    schooling = Column(String(60), index=True)
    address = Column(String(60), index=True)
    income = Column(String(60), index=True)
    marital_status = Column(String(60), index=True)
    imc = Column(Float, index=True)
    group = Column(String(60), index=True)
    vaccination = Column(String(60), index=True)


class NutricionalData(Base):
    __tablename__ = "nutricional_data"

    id = Column(Integer, primary_key=True, index=True)
    nutricional_group = Column(String(60), index=True)


class FrequencyFoodConsumption(Base):
    __tablename__ = "frequency_food_consumption"

    id = Column(Integer, primary_key=True, index=True)
    frequency = Column(String(60), index=True)


class FoodConsumption(Base):
    __tablename__ = 'food_consumption'

    id = Column(Integer, primary_key=True)
    patient_information_id = Column(Integer)
    age_group_id = Column(Integer)
    ethnicity_id = Column(Integer)
    nutritional_data_id = Column(Integer)
    carga_viral = Column(Float)
    comorbity = Column(Text)
    leite = Column(Integer)
    Iogurte = Column(Integer)
    queijo_branco = Column(Integer)
    queijo_amarelo = Column(Integer)
    requeijao = Column(Integer)
    ovo_frito = Column(Integer)
    ovo_cozido = Column(Integer)
    carne_de_boi = Column(Integer)
    carne_de_porco = Column(Integer)
    frango = Column(Integer)
    peixe_fresco = Column(Integer)
    peixe_enlatado = Column(Integer)
    carne_conservada_no_sal = Column(Integer)
    visceras = Column(Integer)
    azeite = Column(Integer)
    bacon_toucinho_banha_de_porco = Column(Integer)
    arroz_integral = Column(Integer)
    arroz_polido = Column(Integer)
    pao_integral = Column(Integer)
    pao_frances = Column(Integer)
    bolo_caseiro = Column(Integer)
    macarrao = Column(Integer)
    feijao = Column(Integer)
    lentilhas = Column(Integer)
    folha_crua = Column(Integer)
    folha_refogada_cozida = Column(Integer)
    legumes_cozidos = Column(Integer)
    tuberculos = Column(Integer)
    frutas = Column(Integer)
    sucos_naturais_sem_acucar = Column(Integer)
    suco_natural_com_acucar = Column(Integer)
    tortas_e_doces = Column(Integer)
    cafe_com_acucar = Column(Integer)
    refrigerante = Column(Integer)
    suco_artificial_com_acucar = Column(Integer)
    adocante = Column(Integer)
    embutidos = Column(Integer)
    molhos_para_salada = Column(Integer)
    manteiga_margarina_maionese = Column(Integer)
    snacks = Column(Integer)
    petiscos = Column(Integer)
    enlatados = Column(Integer)
    pao_de_forma = Column(Integer)
    biscoito_salgado = Column(Integer)
    biscoito_doce = Column(Integer)
    bolo_industrializado = Column(Integer)
    Sorvetes_balas_guloseimas = Column(Integer)
    geleia_industrializadas = Column(Integer)
    chocolate_s_achocolatados = Column(Integer)
    macarrao_instantaneo = Column(Integer)


class Ethnicity(Base):
    __tablename__ = 'ethnicity'

    id = Column(Integer, primary_key=True, index=True)
    group = Column(String(60), index=True)


class CytokinesCovid(Base):
    __tablename__ = 'cytokines_covid'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_information_id = Column(Integer)
    FGF_basic = Column(Float)
    G_CSF = Column(Float)
    GM_CSF = Column(Float)
    PDGF = Column(Float)
    VEGF = Column(Float)
    IL_1_beta = Column(Float)
    IL_6 = Column(Float)
    IL_12p70 = Column(Float)
    IFN_gamma = Column(Float)
    TNF_alpha = Column(Float)
    CCL2 = Column(Float)
    CCL3 = Column(Float)
    CCL4 = Column(Float)
    CCL5 = Column(Float)
    Eotaxin = Column(Float)
    IL_4 = Column(Float)
    IL_5 = Column(Float)
    IL_13 = Column(Float)
    IL_2 = Column(Float)
    IL_10 = Column(Float)
    CXCL10 = Column(Float)
    CXCL8 = Column(Float)
    IL_1ra = Column(Float)
    IL_7 = Column(Float)
    IL_9 = Column(Float)
    IL_15 = Column(Float)
    IL_17 = Column(Float)
    DIS = Column(Integer)


class BloodCountData(Base):
    __tablename__ = 'blood_count_data'

    id = Column(Integer, primary_key=True)
    patient_information_id = Column(Integer)
    leucocitos_WBC = Column(Float)
    contagem_de_hemacias_RBC = Column(Float)
    hemoglobina = Column(Float)
    hematocrito_HCT = Column(String(60))
    MCV = Column(Integer)
    MCH = Column(Float)
    MCHC = Column(Float)
    RDW = Column(String(60))
    granulocitos = Column(String(60))
    monocitos = Column(String(60))
    linfocitos = Column(String(60))
    plaquetas = Column(Integer)
    MPV = Column(Float)
    PDW_variacao_de_tamanho_das_plaquetas = Column(String(60))
    PCT = Column(String(60))
    GLR = Column(String)
    MLR = Column(String)
    PLT_LYM = Column(String(60))
    PLR = Column(String(60))