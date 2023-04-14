from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship, registry


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

    food_consumption = relationship("FoodConsumption", back_populates="patient_information_cvd")
    cytokines_covid = relationship("CytokinesCovid", back_populates="patient_information_cvd")


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
    patient_information_id = Column(Integer, ForeignKey('patient_information_cvd.id'))
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

    patient_information_cvd = relationship("PatientInformationCvd", back_populates="food_consumption")


class Ethnicity(Base):
    __tablename__ = 'ethnicity'

    id = Column(Integer, primary_key=True, index=True)
    group = Column(String(60), index=True)


class CytokinesCovid(Base):
    __tablename__ = 'cytokines_covid'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_information_id = Column(Integer, ForeignKey('patient_information_cvd.id'))
    FGF_basic = Column(Float, name="FGF-basic")
    G_CSF = Column(Float, name="G-CSF")
    GM_CSF = Column(Float, name="GM-CSF")
    PDGF = Column(Float, name="PDGF")
    VEGF = Column(Float, name="VEGF")
    IL_1_beta = Column(Float, name="IL-1-beta")
    IL_6 = Column(Float, name="IL-6")
    IL_12p70 = Column(Float, name="IL-12p70")
    IFN_gamma = Column(Float, name="IFN-gamma")
    TNF_alpha = Column(Float, name="TNF-alpha")
    CCL2 = Column(Float, name="CCL2")
    CCL3 = Column(Float, name="CCL3")
    CCL4 = Column(Float, name="CCL4")
    CCL5 = Column(Float, name="CCL5")
    Eotaxin = Column(Float, name="Eotaxin")
    IL_4 = Column(Float, name="IL-4")
    IL_5 = Column(Float, name="IL-5")
    IL_13 = Column(Float, name="IL-13")
    IL_2 = Column(Float, name="IL-2")
    IL_10 = Column(Float, name="IL-10")
    CXCL10 = Column(Float, name="CXCL10")
    CXCL8 = Column(Float, name="CXCL8")
    IL_1ra = Column(Float, name="IL-1ra")
    IL_7 = Column(Float, name="IL-7")
    IL_9 = Column(Float, name="IL-9")
    IL_15 = Column(Float, name="IL-15")
    IL_17 = Column(Float, name="IL-17")
    DIS = Column(Integer, name="DIS")

    patient_information_cvd = relationship("PatientInformationCvd", back_populates="cytokines_covid")

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