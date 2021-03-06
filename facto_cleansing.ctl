LOAD DATA
CHARACTERSET UTF8
REPLACE
INTO TABLE GPDT_CREDITSAFE_IN
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
	ClientGpRef                           char,
	CustGpRef                             char,
	CustCompany                           char,
	CustAddress1                          char,
	CustAddress2                          char,
	CustAddress3                          char,
	CustCity                              char,
	CustState                             char,
	CustZIP                               char,
	CustCountryCode                       char,
	CustFedId                             char,
	CustPhone                             char,
	11
	12
	13
	14
	15
	16
	17
	18
	19
	20
	21
	22
	23
	DC_CONNECTID                          filler,
	DC_GGSID                              char,
	DC_CONAME                             "substr(:DC_CONAME, 1, 255)",
	DC_REG_NUMBER                         char,
	DC_ORG_NUMBER                         char,
	DC_ADDRESS1                           char,
	DC_ADDRESS2                           char,
	DC_ADDRESS3                           char,
	DC_TOWN                               "trim(:DC_TOWN)",
	DC_POSTCODE                           char,
	DC_REGION                             char,
	DC_PROVINCE_STATE                     char,
	DC_COUNTRY                            char,
	DC_COMPANY_TYPE                       filler,
	DC_COMPANY_TYPE_DESCRIPTION           filler,
	DC_PHONE                              "trim(:DC_PHONE)",
	DC_SIC_CODE                           filler,
	DC_SIC_DESC                           filler,
	DC_LEGAL_FORM                         char,
	DC_LEGAL_FORM_DESC                    filler,
	DC_CURRENCY                           char,
	DC_CREDIT_SCORE                       char,
	DC_LIMIT                              char,
	DC_INTERNATIONAL_SCORE                char,
	DC_CREDITWORTHY                       char,
	DC_DBT                                filler,
	DC_TURNOVER                           char,
	DC_LATEST_ACCOUNTS                    char (1000),
	DC_DIRECTORS_FULL_NAME                char (2000),
	DC_SAFENUMBER                         char,
	ALGORITHM                             char,
	DC_ALGORITHM_BANDING                  filler,
	DC_ALGORITHM_DESCRIPTION              filler
)
