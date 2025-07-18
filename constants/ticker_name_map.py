class Tickers:
     
     ticker_json = {
                     "MASPTOP50.NS": "S&P 500 Top 50 Total Return Index",
                     "FMCGIETF.NS": "Nifty FMCG Index",
                     "MAFANG.NS": "NYSE FANG+ Total Return Index",
                     "MOLOWVOL.NS": "Nifty Midcap 100 TRI",
                     "CONSUMIETF.NS": "Nifty India Consumption Index",
                     "OILIETF.NS": "Nifty Oil & Gas Index",
                     "ECAPINSURE.NS": "BSE Capital Markets & Insurance Total Return Index",
                     "AXISCETF.NS": "NIFTY India Consumption Index",
                     "LICNETFSEN.NS": "SENSEX",
                     "AXSENSEX.NS": "AXIS S&P BSE SENSEX ETF",
                     "QUAL30IETF.NS": "ICICI Prudential Nifty 200 Quality 30 ETF",
                     "CONSUMBEES.NS": "Nifty India Consumption TRI",
                     "HDFCNEXT50.NS": "HDFC NIFTY NEXT 50 ETF",
                     "UTISXN50.NS": "BSE Sensex Next 50",
                     "LOWVOL.NS": "Mirae Asset Nifty 100 Low Volatility 30 ETF",
                     "SBIETFCON.NS": "Nifty India Consumption Index",
                     "HDFCLOWVOL.NS": "HDFC NIFTY100 Low Volatility 30 ETF",
                     "GROWWMOM50.NS": "Nifty 500 Momentum 50 Index- Total Return Index",
                     "LOWVOLIETF.NS": "Nifty 100 Low Volatility 30 Index",
                     "MOINFRA.NS": "BSE India Infrastructure Total Return Index",
                     "LICNFNHGP.NS": "Nifty 100",
                     "IDFNIFTYET.NS": "Nifty 50",
                     "NEXT30ADD.NS": "BSE SENSEX Next 30 Index",
                     "MOM50.NS": "Nifty 50",
                     "MOHEALTH.NS": "Motilal Oswal S&P BSE Healthcare ETF",
                     "MON100.NS": "Nasdaq100",
                     "HEALTHADD.NS": "DSP Nifty Healthcare ETF",
                     "INFRAIETF.NS": "ICICI Prudential Nifty Infrastructure ETF",
                     "QNIFTY.NS": "Nifty 50",
                     "ALPL30IETF.NS": "Nifty Alpha Low-Volatility 30 Index",
                     "DIVOPPBEES.NS": "Nifty Dividend Opportunities 50 TRI",
                     "GROWWSLVR.NS": "Commodity-Silver",
                     "NEXT50IETF.NS": "Nifty Next 50",
                     "HDFCNIFTY.NS": "Nifty 50",
                     "HDFCNIF100.NS": "HDFC NIFTY 100 ETF",
                     "TOP15IETF.NS": "Nifty Top 15 Equal Weight Index",
                     "AONENIFTY.NS": "Nifty 50 Index",
                     "NEXT50.NS": "Nifty Next 50",
                     "UTINIFTETF.NS": "Nifty 50",
                     "HDFCGROWTH.NS": "HDFC NIFTY Growth Sectors 15 ETF",
                     "AONETOTAL.NS": "Nifty Total Market Index",
                     "SBISILVER.NS": "SBI SILVER ETF",
                     "SENSEXIETF.NS": "SENSEX",
                     "UTINEXT50.NS": "Nifty Next 50",
                     "NIFTY100EW.NS": "Nifty 100 Equal Weight Index",
                     "MONEXT50.NS": "Nifty Next 50 Total Return Index",
                     "TOP10ADD.NS": "Nifty Top 10 Equal Weight Index",
                     "NIFTYQLITY.NS": "Aditya Birla Sun Life Nifty 200 Quality 30 ETF",
                     "INFRABEES.NS": "Nifty Infra",
                     "UTISENSETF.NS": "SENSEX",
                     "HDFCBSE500.NS": "HDFC S&P BSE 500 ETF",
                     "BSE500IETF.NS": "S&P BSE 500 index",
                     "SHARIABEES.NS": "Shariah",
                     "TATSILV.NS": "Tata Silver Exchange Traded Fund",
                     "SILVERETF.NS": "UTI Silver Exchange Traded Fund (UTI Silver ETF)",
                     "FINIETF.NS": "ICICI Prudential Nifty Financial Services Ex-Bank ETF",
                     "HDFCQUAL.NS": "HDFC NIFTY100 Quality 30 ETF",
                     "TOP100CASE.NS": "Zerodha Nifty 100 ETF",
                     "SENSEXETF.NS": "Mirae Asset S&P BSE Sensex ETF",
                     "AXISBPSETF.NS": "Nifty AAA Bond Plus SDL Apr 2026 50:50 Index",
                     "NIF100IETF.NS": "Nifty 100",
                     "AXISILVER.NS": "Axis Silver ETF",
                     "MOMGF.NS": "Nifty India Manufacturing Total Return Index",
                     "GROWWEV.NS": "Nifty EV and New Age Automotive Index",
                     "LICNETFGSC.NS": "GSEC10 NSE Index",
                     "ESILVER.NS": "Edelweiss Silver ETF",
                     "MOVALUE.NS": "Motilal Oswal S&P BSE Enhanced Value ETF",
                     "EQUAL50.NS": "Nifty50 Equal Weight",
                     "SBIBPB.NS": "BSE PSU Bank Index TRI",
                     "NIF10GETF.NS": "UTI Nifty 10 yr Benchmark G-Sec ETF",
                     "NIFTYBEES.NS": "Nifty 50",
                     "HDFCPVTBAN.NS": "HDFC NIFTY Private Bank ETF",
                     "MONIFTY500.NS": "Motilal Oswal Nifty 500 ETF",
                     "MIDCAP.NS": "Nifty Midcap 50 Index",
                     "JUNIORBEES.NS": "Nippon India ETF Nifty Next 50 Junior BeES",
                     "SNXT30BEES.NS": "BSE Sensex Next 30 Index",
                     "EVINDIA.NS": "Nifty EV and New Age Automotive Total Return Index",
                     "MNC.NS": "Kotak Nifty MNC ETF",
                     "EQUAL50ADD.NS": "NIFTY 50 Equal Weight Index",
                     "MAKEINDIA.NS": "Nifty India Manufacturing Total Return Index",
                     "MID150BEES.NS": "Nifty Midcap 150 TRI",
                     "NIFTYIETF.NS": "Nifty 50",
                     "ESG.NS": "NIFTY100 ESG SECTOR LEADERS",
                     "SILVER1.NS": "Kotak Silver ETF",
                     "SBIETFQLTY.NS": "Nifty 200 Quality 30 Index",
                     "NIFTYBETF.NS": "Bajaj Finserv Nifty 50 ETF",
                     "SETFNN50.NS": "Nifty Next 50",
                     "CASHIETF.NS": "BSE Liquid Rate Index",
                     "PVTBANIETF.NS": "Nifty Private Bank Index",
                     "PHARMABEES.NS": "Nifty Pharma TRI",
                     "NETF.NS": "Tata Nifty 50 Exchange Traded Fund",
                     "AXISNIFTY.NS": "Nifty 50",
                     "EMULTIMQ.NS": "Nifty500 Multicap Momentum Quality 50 Total Return Index",
                     "MSCIINDIA.NS": "MSCI India Index",
                     "AXISVALUE.NS": "Nifty500 Value 50 TRI",
                     "GROWWN200.NS": "Nifty 200 Index- Total Return Index",
                     "BBNPNBETF.NS": "Baroda BNP Paribas NIFTY Bank ETF",
                     "MID150CASE.NS": "Zerodha Nifty Midcap 150 ETF",
                     "BFSI.NS": "Nifty Financial Services Index",
                     "NV20.NS": "Nifty50 Value 20",
                     "LICNETFN50.NS": "Nifty 50",
                     "AXISHCETF.NS": "Nifty Healthcare Index",
                     "NIFITETF.NS": "UTI Nifty IT ETF",
                     "LICMFGOLD.NS": "Gold",
                     "NIFTY50ADD.NS": "Nifty 50 Index",
                     "PVTBANKADD.NS": "DSP Nifty Private Bank ETF",
                     "GROWWRAIL.NS": "Nifty India Railways PSU Index",
                     "NIFTY1.NS": "Nifty 50",
                     "SILVERBEES.NS": "Domestic price of Silver- based on LBMA Silver daily spot fixing price",
                     "MOM30IETF.NS": "ICICI Prudential Nifty 200 Momentum 30 ETF",
                     "ABSLNN50ET.NS": "Nifty Next 50",
                     "PSUBANKADD.NS": "DSP Nifty PSU Bank ETF",
                     "HEALTHY.NS": "Nifty Healthcare TRI",
                     "NIF100BEES.NS": "Nifty 100 TRI",
                     "MOPSE.NS": "Nifty PSE Total Return Index",
                     "EQUAL200.NS": "BSE 200 Equal Weight",
                     "HDFCMOMENT.NS": "HDFC NIFTY200 Momentum 30 ETF",
                     "SBIETFPB.NS": "Nifty Private Bank Index",
                     "HDFCSILVER.NS": "HDFC Silver ETF",
                     "SILVERIETF.NS": "Domestic Price of Silver",
                     "SILVRETF.NS": "Mirae Asset Silver ETF",
                     "GROWWGOLD.NS": "Commodity",
                     "HDFCNIFBAN.NS": "Nifty Bank",
                     "ABSLPSE.NS": "Aditya Birla Sun Life Nifty PSE ETF",
                     "ICICIB22.NS": "S&P BSE BHARAT 22 index",
                     "BANKNIFTY1.NS": "Nifty Bank",
                     "MOSMALL250.NS": "Motilal Oswal Nifty Smallcap 250 ETF",
                     "IVZINGOLD.NS": "Gold",
                     "MULTICAP.NS": "Nifty500 Multicap 50:25:25 Index",
                     "SBINEQWETF.NS": "Nifty50 Equal Weight",
                     "CONS.NS": "Kotak Nifty India Consumption ETF",
                     "MOMOMENTUM.NS": "Nifty 200 Momentum 30 Total Return Index",
                     "AUTOBEES.NS": "Nifty Auto TRI",
                     "SILVER.NS": "Physical price of Silver",
                     "IVZINNIFTY.NS": "Nifty 50",
                     "BANKPSU.NS": "Nifty PSU Bank Total Return Index",
                     "NV20IETF.NS": "Nifty50 Value 20",
                     "LOWVOL1.NS": "Kotak Nifty 100 Low Vol 30 ETF",
                     "NIFTYETF.NS": "Nifty 50",
                     "HDFCSML250.NS": "HDFC NIFTY Smallcap 250 ETF",
                     "EGOLD.NS": "Edelweiss Gold ETF",
                     "AXISBNKETF.NS": "Nifty Bank",
                     "SETFNIFBK.NS": "Nifty Bank",
                     "SETFNIF50.NS": "Nifty 50",
                     "BANKETFADD.NS": "DSP Nifty Bank ETF",
                     "BANKBETF.NS": "Bajaj Finserv Nifty Bank ETF",
                     "EBANKNIFTY.NS": "Edelweiss Nifty Bank ETF",
                     "BSLNIFTY.NS": "Nifty 50",
                     "CONSUMER.NS": "Nifty India New AgeConsumption",
                     "SILVERCASE.NS": "Commodity-Silver",
                     "BANKIETF.NS": "Nifty Bank",
                     "HDFCVALUE.NS": "HDFC NIFTY50 Value 20 ETF",
                     "SELECTIPO.NS": "BSE Select IPO Index",
                     "MONQ50.NS": "Nasdaq Q-50 Total Return Index",
                     "NV20BEES.NS": "Nifty50 Value20 TRI",
                     "ABSLBANETF.NS": "Nifty Bank",
                     "MON50EQUAL.NS": "Nifty 50 Equal Weight Total Return Index",
                     "VAL30IETF.NS": "Nifty200 Value 30 Index",
                     "BANKBEES.NS": "Nifty Bank",
                     "COMMOIETF.NS": "ICICI Prudential Nifty Commodities ETF",
                     "MIDCAPIETF.NS": "Nifty Midcap 150",
                     "GOLDSHARE.NS": "Gold",
                     "AUTOIETF.NS": "Nifty Auto Index",
                     "MOCAPITAL.NS": "Nifty Capital Market Total Return Index",
                     "UTIBANKETF.NS": "Nifty Bank",
                     "UNIONGOLD.NS": "Commodity Gold",
                     "MOM100.NS": "Nifty Midcap 100",
                     "ALPHAETF.NS": "Mirae Asset Nifty 200 Alpha 30 ETF",
                     "LICNMID100.NS": "LIC MF Nifty Midcap 100 ETF",
                     "GROWWLOVOL.NS": "Nifty 500 Low Volatility 50 Index \ufffd TRI",
                     "QGOLDHALF.NS": "Gold",
                     "BANKETF.NS": "Mirae Asset Nifty Bank ETF",
                     "GOLDIETF.NS": "Gold",
                     "MOMENTUM50.NS": "Nifty 500 Momentum 50 Total Return Index",
                     "PSUBNKBEES.NS": "Nifty PSU Bank",
                     "MOREALTY.NS": "Motilal Oswal Nifty Realty ETF",
                     "SETFGOLD.NS": "Gold",
                     "HDFCMID150.NS": "HDFC NIFTY Midcap 150 ETF",
                     "TATAGOLD.NS": "Tata Gold Exchange Traded Fund",
                     "MIDSMALL.NS": "Mirae Asset Nifty MidSmallcap400 Momentum Quality 100 ETF",
                     "GOLDCASE.NS": "Zerodha Gold ETF",
                     "SILVERADD.NS": "DSP Silver ETF",
                     "HDFCSENSEX.NS": "SENSEX",
                     "PSUBANK.NS": "Nifty PSU Bank",
                     "BSLSENETFG.NS": "BSE SENSEX Index",
                     "HDFCPSUBK.NS": "HDFC NIFTY PSU BANK ETF",
                     "HEALTHIETF.NS": "Nifty Healthcare Index",
                     "GOLD360.NS": "Commodity-Gold",
                     "MAHKTECH.NS": "Hang Seng TECH Total Return Index",
                     "HDFCGOLD.NS": "Gold",
                     "MIDCAPETF.NS": "Mirae Asset Mutual Fund - Mirae Asset Nifty Midcap 150 ETF",
                     "SMALLCAP.NS": "Mirae Asset Nifty Smallcap 250 Momentum Quality 100 ETF",
                     "NIF5GETF.NS": "UTI Nifty 5 yr Benchmark G-Sec ETF",
                     "BBNPPGOLD.NS": "Baroda BNP Paribas Gold ETF",
                     "AXISGOLD.NS": "Gold",
                     "PSUBNKIETF.NS": "ICICI Prudential Nifty PSU Bank ETF",
                     "MOQUALITY.NS": "Motilal Oswal S&P BSE Quality ETF",
                     "MOMIDMTM.NS": "Nifty Midcap 150 Momentum 50 Total Return Index",
                     "GOLD1.NS": "Gold",
                     "METAL.NS": "Nifty Metal Total Return Index",
                     "MIDSELIETF.NS": "S&P BSE Midcap Select Index",
                     "MID150.NS": "Nifty Midcap 150 Index",
                     "SENSEXADD.NS": "DSP S&P BSE Sensex ETF",
                     "GOLDBEES.NS": "Gold",
                     "MIDQ50ADD.NS": "Nifty Midcap 150 Quality 50 Index",
                     "HNGSNGBEES.NS": "Hang Seng Index",
                     "SDL26BEES.NS": "Nifty SDL Apr 2026 Top 20 Equal Weight Index",
                     "NPBET.NS": "Nifty Private Bank Index",
                     "GROWWNET.NS": "Index",
                     "MOMENTUM.NS": "Aditya Birla Sun Life Nifty 200 Momentum 30 ETF",
                     "ALPHA.NS": "NIFTY Alpha 50 Index",
                     "METALIETF.NS": "Nifty Metal Index",
                     "CPSEETF.NS": "CPSE ETF",
                     "ITBEES.NS": "Nifty IT TRI",
                     "GOLDETF.NS": "Mirae Asset Gold ETF",
                     "SILVER360.NS": "Commodity-Silver",
                     "AXISTECETF.NS": "NIFTY IT Index",
                     "MOTOUR.NS": "Nifty India Tourism Total Return Index",
                     "TECH.NS": "Nifty IT TRI Index",
                     "IT.NS": "NIFTY IT Index",
                     "ITIETF.NS": "Nifty IT Index",
                     "NIFMID150.NS": "UTI Nifty Midcap 150 Exchange Traded Fund (ETF)",
                     "BSLGOLDETF.NS": "Gold",
                     "GOLDETFADD.NS": "DSP Gold ETF",
                     "TNIDETF.NS": "Nifty India Digital Index",
                     "MODEFENCE.NS": "Nifty India Defence Total Return Index",
                     "GROWWDEFNC.NS": "Nifty India Defence Index- Total Return Index",
                     "ITETFADD.NS": "DSP Nifty IT ETF",
                     "HDFCNIFIT.NS": "HDFC NIFTY IT ETF",
                     "ITETF.NS": "Mirae Asset Nifty IT ETF",
                     "SBIETFIT.NS": "Nifty IT Index",
                     "EVIETF.NS": "Nifty EV & New Age Automotive ETF"
                     }
     tickessr_json =  { "MON100.NS": "Nasdaq100", }
     __ticker_json =  {
            "BTC-USD" : "BTC-USD",
            # "0P0000XW51.BO": "Quant ELSS Tax Saver Fund MF",
            # "0P00017844.BO": "Mirae Asset ELSS Tax Saver Fund MF",
            # "0P00005VCS.BO": "HSBC ELSS Tax Saver Fund MF",
            # "0P0000XVU7.BO": "Axis ELSS Tax Saver Fund MF",
            # "0P0000XV1I.BO": "Bandhan ELSS Tax Saver Fund MF",
            # "0P0001R64W.BO": "Motilal Oswal Nifty Microcap 250 Index Fund MF",
            # "0P0000XVDP.BO": "Nippon India Growth Direct Growth MF",
            # "0P0001RQX5.BO": "Zerodha Nifty LargeMidcap 250 Index Fund Tax Saver Dir Gr MF",
            # "0P0000GB29.BO": "Aditya BSL ELSS Tax Saver Gr MF",
            # "0P0000XW04.BO": "Canara Robeco ELSS Tax Saver Dir Gr MF",
            # "0P00011MAX.BO": "Axis Small Cap Fund Dir Gr MF",
            # "0P000159Q2.BO": "Motilal Oswal ELSS Tax Saver Reg Gr MF",
            # "0P00009J3K.BO": "HDFC Mid-Cap Opportunities Gr MF",
            # "0P0000XVFY.BO": "Nippon India Small Cap Dir Gr MF",
            # "0P00008TPO.BO": "Kotak Emerging Equity Scheme MF",
            # "0P0000XW1B.BO": "SBI Small Cap Fund Dir Gr MF",
            # "0P0000XVUH.BO": "Axis Midcap Fund Dir Gr MF",
            # "0P00012ALU.BO": "Motilal Oswal Midcap Reg Gr MF",
            # "0P0000XW4X.BO": "Quant Small Cap Fund MF",
            # "0P00012ALS.BO": "Motilal Oswal Midcap Dir Gr MF",
            # "0P0000XW2T.BO": "DSP ELSS Tax Saver Dir Gr MF",
            # "0P0000YK1E.BO": "ICICI Pru Thematic Advantage dir  MF",
            # "0P0000XVXV.BO": "Aditya BSL Digital India Dir Gr MF",
            # "0P0001BA2I.BO": "Edelweiss Mid Cap Fund MF",
            # "0P0000IQJ7.BO": "Quant Flexi Cap Fund MF",
            # "0P0000XW4V.BO": "Quant Mid Cap Dir Gr MF",
            # "0P0000XVAA.BO": "HDFC Small Cap Dir Gr MF",
            # "0P0000XUZ6.BO": "ICICI Pru Technology Dir Gr MF",
            # "0P0000XV5R.BO": "Kotak Emerging Equity Dir Gr MF",
            # "0P000093TC.BO": "Invesco India Mid Cap Gr MF",
            # "0P0000XW4E.BO": "Quant Active Dir Gr MF",
            # "0P0000YWL1.BO" : "Parag Parikh Long Term Equity Direct Growth MF",
            # "0P0000XW8F.BO" : "HDFC Mid-Cap Opportunities Dir Gr MF",
            # "0P0000XW24.BO" : "DSP Small Cap Dir Gr MF",
            # "0P0000XV9V.BO" : "Mirae Asset Large & Midcap Dir Gr MF",
            # "0P0000XVKP.BO" : "SBI Technology Opportunities Dir Gr MF",
            # "0P0000XW5R.BO" : "Franklin India Technology Dir Gr MF",
            # "0P0000XW4F.BO" : "Quant Large and Mid Cap Dir MF",
            # "0P0000XVDP.BO" : "Nippon India Growth Dir Gr MF",
            # "0P0000XW51.BO" : "Quant ELSS Tax Saver Dir Gr MF",
            # "0P0000XVZR.BO" : "Bank of India ELSS Tax Saver Dir MF",
            # "0P0001F5O4.BO" : "Bank of India Small Cap Dir Gr MF",
            # "0P0001FKEE.BO" : "Canara Rob Small Cap Fund Dir Gr MF",
            # "0P0001FI5D.BO"	: "Edelweiss Small Cap Fund Regular Growth MF",
            # "0P0001EUZZ.BO" : "Tata Small Cap Fund Direct Growth MF",
            # "0P0001F1DY.BO" : "Dsp Healthcare Fund Direct Growth MF",
            # "0P0001EQU4.BO" : "Invesco India Smallcap Fund Dir Growth MF",
            # "0P0001HZ17.BO" : "Parag Parikh ELSS Tax Saver Fund Fir G MF",

           "ITETFADD.NS": "DSP Nifty IT ETF",
    "FINIETF.NS": "ICICI Prudential Nifty Financial Services Ex-Bank ETF",
    "MOCAPITAL.NS": "Nifty Capital Market Total Return Index",
    "CONS.NS": "Kotak Nifty India Consumption ETF",
    "MIDQ50ADD.NS": "Nifty Midcap 150 Quality 50 Index",
    "HDFCNIFIT.NS": "HDFC NIFTY IT ETF",
    "EQUAL50.NS": "Nifty50 Equal Weight",
    "ECAPINSURE.NS": "BSE Capital Markets & Insurance Total Return Index",
    "AXISTECETF.NS": "NIFTY IT Index",
    "SBIETFIT.NS": "Nifty IT Index",
    "NPBET.NS": "Nifty Private Bank Index",
    "FMCGIETF.NS": "Nifty FMCG Index",
    "ESG.NS": "NIFTY100 ESG SECTOR LEADERS",
    "MOM50.NS": "Nifty 50",
    "NEXT30ADD.NS": "BSE SENSEX Next 30 Index",
    "SENSEXIETF.NS": "SENSEX",
    "QUAL30IETF.NS": "ICICI Prudential Nifty 200 Quality 30 ETF",
    "MAFANG.NS": "NYSE FANG+ Total Return Index",
    "GROWWN200.NS": "Nifty 200 Index- Total Return Index",
    "HDFCNIF100.NS": "HDFC NIFTY 100 ETF",
    "HDFCLOWVOL.NS": "HDFC NIFTY100 Low Volatility 30 ETF",
    "LICNETFN50.NS": "Nifty 50",
    "QNIFTY.NS": "Nifty 50",
    "ITBEES.NS": "Nifty IT TRI",
    "DIVOPPBEES.NS": "Nifty Dividend Opportunities 50 TRI",
    "MON50EQUAL.NS": "Nifty 50 Equal Weight Total Return Index",
    "ICICIB22.NS": "S&P BSE BHARAT 22 index",
    "SBINEQWETF.NS": "Nifty50 Equal Weight",
    "CONSUMBEES.NS": "Nifty India Consumption TRI",
    "MONQ50.NS": "Nasdaq Q-50 Total Return Index",
    "HDFCNIFTY.NS": "Nifty 50",
    "TOP10ADD.NS": "Nifty Top 10 Equal Weight Index",
    "SENSEXETF.NS": "Mirae Asset S&P BSE Sensex ETF",
    "LOWVOL.NS": "Mirae Asset Nifty 100 Low Volatility 30 ETF",
    "HDFCVALUE.NS": "HDFC NIFTY50 Value 20 ETF",
    "MSCIINDIA.NS": "MSCI India Index",
    "ITIETF.NS": "Nifty IT Index",
    "NV20BEES.NS": "Nifty50 Value20 TRI",
    "CONSUMIETF.NS": "Nifty India Consumption Index",
    "OILIETF.NS": "Nifty Oil & Gas Index",
    "HDFCQUAL.NS": "HDFC NIFTY100 Quality 30 ETF",
    "HDFCSENSEX.NS": "SENSEX",
    "LOWVOLIETF.NS": "Nifty 100 Low Volatility 30 Index",
    "NIFTYETF.NS": "Nifty 50",
    "NIF100IETF.NS": "Nifty 100",
    "SBIBPB.NS": "BSE PSU Bank Index TRI",
    "MOMENTUM.NS": "Aditya Birla Sun Life Nifty 200 Momentum 30 ETF",
    "TNIDETF.NS": "Nifty India Digital Index",
    "SBIETFPB.NS": "Nifty Private Bank Index",
    "NIFTYBEES.NS": "Nifty 50",
    "BSLSENETFG.NS": "BSE SENSEX Index",
    "ALPHA.NS": "NIFTY Alpha 50 Index",
    "BSLNIFTY.NS": "Nifty 50",
    "AXISNIFTY.NS": "Nifty 50",
    "MID150BEES.NS": "Nifty Midcap 150 TRI",
    "SETFNIF50.NS": "Nifty 50",
    "MOM30IETF.NS": "ICICI Prudential Nifty 200 Momentum 30 ETF",
    "SBIETFCON.NS": "Nifty India Consumption Index",
    "HDFCPVTBAN.NS": "HDFC NIFTY Private Bank ETF",
    "NETF.NS": "Tata Nifty 50 Exchange Traded Fund",
    "BANKBEES.NS": "Nifty Bank",
    "EQUAL50ADD.NS": "NIFTY 50 Equal Weight Index",
    "BANKPSU.NS": "Nifty PSU Bank Total Return Index",
    "ABSLBANETF.NS": "Nifty Bank",
    "MIDCAP.NS": "Nifty Midcap 50 Index",
    "NIFTYIETF.NS": "Nifty 50",
    "SETFNN50.NS": "Nifty Next 50",
    "ALPHAETF.NS": "Mirae Asset Nifty 200 Alpha 30 ETF",
    "BANKETFADD.NS": "DSP Nifty Bank ETF",
    "HDFCSML250.NS": "HDFC NIFTY Smallcap 250 ETF",
    "SETFNIFBK.NS": "Nifty Bank",
    "GROWWMOM50.NS": "Nifty 500 Momentum 50 Index- Total Return Index",
    "HDFCMID150.NS": "HDFC NIFTY Midcap 150 ETF",
    "NIF100BEES.NS": "Nifty 100 TRI",
    "TOP100CASE.NS": "Zerodha Nifty 100 ETF",
    "MOLOWVOL.NS": "Nifty Midcap 100 TRI",
    "BANKIETF.NS": "Nifty Bank",
    "COMMOIETF.NS": "ICICI Prudential Nifty Commodities ETF",
    "SHARIABEES.NS": "Shariah",
    "AXISBNKETF.NS": "Nifty Bank",
    "NIFTYBETF.NS": "Bajaj Finserv Nifty 50 ETF",
    "IDFNIFTYET.NS": "Nifty 50",
    "BANKBETF.NS": "Bajaj Finserv Nifty Bank ETF",
    "HDFCNIFBAN.NS": "Nifty Bank",
    "NIFMID150.NS": "UTI Nifty Midcap 150 Exchange Traded Fund (ETF)",
    "UTINEXT50.NS": "Nifty Next 50",
    "BANKNIFTY1.NS": "Nifty Bank",
    "AXISCETF.NS": "NIFTY India Consumption Index",
    "MID150CASE.NS": "Zerodha Nifty Midcap 150 ETF",
    "UTIBANKETF.NS": "Nifty Bank",
    "HDFCBSE500.NS": "HDFC S&P BSE 500 ETF",
    "NEXT50IETF.NS": "Nifty Next 50",
    "PVTBANIETF.NS": "Nifty Private Bank Index",
    "CPSEETF.NS": "CPSE ETF",
    "METAL.NS": "Nifty Metal Total Return Index",
    "SELECTIPO.NS": "BSE Select IPO Index",
    "NIFTY50ADD.NS": "Nifty 50 Index",
    "UTINIFTETF.NS": "Nifty 50",
    "PSUBANKADD.NS": "DSP Nifty PSU Bank ETF",
    "BSE500IETF.NS": "S&P BSE 500 index",
    "EBANKNIFTY.NS": "Edelweiss Nifty Bank ETF",
    "HDFCMOMENT.NS": "HDFC NIFTY200 Momentum 30 ETF",
    "AXISVALUE.NS": "Nifty500 Value 50 TRI",
    "AONETOTAL.NS": "Nifty Total Market Index",
    "MOSMALL250.NS": "Motilal Oswal Nifty Smallcap 250 ETF",
    "MIDCAPIETF.NS": "Nifty Midcap 150",
    "MOVALUE.NS": "Motilal Oswal S&P BSE Enhanced Value ETF",
    "IT.NS": "NIFTY IT Index",
    "SMALLCAP.NS": "Mirae Asset Nifty Smallcap 250 Momentum Quality 100 ETF",
    "ABSLPSE.NS": "Aditya Birla Sun Life Nifty PSE ETF",
    "MOMENTUM50.NS": "Nifty 500 Momentum 50 Total Return Index",
    "MAKEINDIA.NS": "Nifty India Manufacturing Total Return Index",
    "UTISENSETF.NS": "SENSEX",
    "ABGSEC.NS": "Aditya Birla Sun Life CRISIL Broad Based Gilt ETF",
    "MASPTOP50.NS": "S&P 500 Top 50 Total Return Index",
    "AXSENSEX.NS": "AXIS S&P BSE SENSEX ETF",
    "NV20IETF.NS": "Nifty50 Value 20",
    "MOINFRA.NS": "BSE India Infrastructure Total Return Index",
    "METALIETF.NS": "Nifty Metal Index",
    "GROWWDEFNC.NS": "Nifty India Defence Index- Total Return Index",
    "BFSI.NS": "Nifty Financial Services Index",
    "SENSEXADD.NS": "DSP S&P BSE Sensex ETF",
    "NV20.NS": "Nifty50 Value 20",
    "ITETF.NS": "Mirae Asset Nifty IT ETF",
    "BBNPNBETF.NS": "Baroda BNP Paribas NIFTY Bank ETF",
    "MOMOMENTUM.NS": "Nifty 200 Momentum 30 Total Return Index",
    "MOM100.NS": "Nifty Midcap 100",
    "BANKETF.NS": "Mirae Asset Nifty Bank ETF",
    "JUNIORBEES.NS": "Nippon India ETF Nifty Next 50 Junior BeES",
    "NEXT50.NS": "Nifty Next 50",
    "INFRAIETF.NS": "ICICI Prudential Nifty Infrastructure ETF",
    "MIDSMALL.NS": "Mirae Asset Nifty MidSmallcap400 Momentum Quality 100 ETF",
    "PSUBNKIETF.NS": "ICICI Prudential Nifty PSU Bank ETF",
    "IVZINNIFTY.NS": "Nifty 50",
    "BSLGOLDETF.NS": "Gold",
    "LICNMID100.NS": "LIC MF Nifty Midcap 100 ETF",
    "NIFTY1.NS": "Nifty 50",
    "NIFTY100EW.NS": "Nifty 100 Equal Weight Index",
    "NIFTYQLITY.NS": "Aditya Birla Sun Life Nifty 200 Quality 30 ETF",
    "ABSLNN50ET.NS": "Nifty Next 50",
    "MNC.NS": "Kotak Nifty MNC ETF",
    "MIDSELIETF.NS": "S&P BSE Midcap Select Index",
    "VAL30IETF.NS": "Nifty200 Value 30 Index",
    "MAHKTECH.NS": "Hang Seng TECH Total Return Index",
    "MULTICAP.NS": "Nifty500 Multicap 50:25:25 Index",
    "TECH.NS": "Nifty IT TRI Index",
    "HEALTHIETF.NS": "Nifty Healthcare Index",
    "MONIFTY500.NS": "Motilal Oswal Nifty 500 ETF",
    "PSUBANK.NS": "Nifty PSU Bank",
    "CONSUMER.NS": "Nifty\uffa0India\uffa0New\uffa0Age\uffa0Consumption",
    "SBIETFQLTY.NS": "Nifty 200 Quality 30 Index",
    "INFRABEES.NS": "Nifty Infra",
    "GSEC5IETF.NS": "Nifty 5 yr Benchmark G-Sec Index",
    "ALPL30IETF.NS": "Nifty Alpha Low-Volatility 30 Index",
    "HDFCGROWTH.NS": "HDFC NIFTY Growth Sectors 15 ETF",
    "LOWVOL1.NS": "Kotak Nifty 100 Low Vol 30 ETF",
    "EVINDIA.NS": "Nifty EV and New Age Automotive Total Return Index",
    "MIDCAPETF.NS": "Mirae Asset Mutual Fund - Mirae Asset Nifty Midcap 150 ETF",
    "EQUAL200.NS": "BSE 200 Equal Weight",
    "MOQUALITY.NS": "Motilal Oswal S&P BSE Quality ETF",
    "EBBETF0433.NS": "BHARAT Bond ETF-April 2033",
    "HDFCPSUBK.NS": "HDFC NIFTY PSU BANK ETF",
    "NIFITETF.NS": "UTI Nifty IT ETF",
    "GROWWEV.NS": "Nifty EV and New Age Automotive Index",
    "MONEXT50.NS": "Nifty Next 50 Total Return Index",
    "HEALTHY.NS": "Nifty Healthcare TRI",
    "SETF10GILT.NS": "Nifty 10 yr Benchmark G-Sec Index",
    "PSUBNKBEES.NS": "Nifty PSU Bank",
    "AXISHCETF.NS": "Nifty Healthcare Index",
    "BBETF0432.NS": "Nifty BHARAT Bond Index - April 2032",
    "AUTOBEES.NS": "Nifty Auto TRI",
    "AUTOIETF.NS": "Nifty Auto Index",
    "MOHEALTH.NS": "Motilal Oswal S&P BSE Healthcare ETF",
    "GOLD1.NS": "Gold",
    "NIF5GETF.NS": "UTI Nifty 5 yr Benchmark G-Sec ETF",
    "LTGILTBEES.NS": "NIFTY 8-13 yr G-Sec Index",
    "GROWWSLVR.NS": "Commodity-Silver",
    "MOREALTY.NS": "Motilal Oswal Nifty Realty ETF",
    "HDFCNEXT50.NS": "HDFC NIFTY NEXT 50 ETF",
    "LIQUIDCASE.NS": "Zerodha Nifty 1D Rate Liquid ETF",
    "GROWWLIQID.NS": "Nifty 1D Rate Index",
    "GSEC10IETF.NS": "ICICI Prudential Nifty 10 yr Benchmark G-Sec ETF",
    "LIQUIDBETF.NS": "Bajaj Finserv Nifty 1D Rate Liquid ETF",
    "LIQUIDPLUS.NS": "Nifty 1D Rate Index",
    "CASHIETF.NS": "BSE Liquid Rate Index",
    "AONELIQUID.NS": "Nifty\uffa01D Rate Index",
    "EMULTIMQ.NS": "Nifty500 Multicap Momentum Quality 50 Total Return Index",
    "LIQUID1.NS": "Kotak Nifty 1D Rate Liquid ETF",
    "HDFCLIQUID.NS": "HDFC Nifty 1D Rate Liquid ETF",
    "EBBETF0431.NS": "Nifty BHARAT Bond",
    "LIQUIDADD.NS": "DSP S&P BSE Liquid Rate ETF",
    "NIF10GETF.NS": "UTI Nifty 10 yr Benchmark G-Sec ETF",
    "LIQUIDSHRI.NS": "SHRIRAM NIFTY 1D RATE LIQUID ETF",
    "GSEC10YEAR.NS": "Mirae Asset Nifty 8-13 yr G-Sec ETF",
    "SDL26BEES.NS": "Nifty SDL Apr 2026 Top 20 Equal Weight Index",
    "HEALTHADD.NS": "DSP Nifty Healthcare ETF",
    "EBBETF0430.NS": "Nifty BHARAT Bond",
    "ABSLLIQUID.NS": "Aditya Birla Sun Life CRISIL Overnight Fund AI ETF",
    "LIQUIDSBI.NS": "SBI NIFTY 1D Rate ETF",
    "LIQUIDBEES.NS": "Government Securities",
    "LIQUID.NS": "Mirae Asset Nifty 1D Rate Liquid ETF",
    "LIQUIDETF.NS": "Nifty1D rate index",
    "TATAGOLD.NS": "Tata Gold Exchange Traded Fund",
    "GOLDSHARE.NS": "Gold",
    "LIQUIDIETF.NS": "S&P BSE Liquid Rate Index",
    "AXISBPSETF.NS": "Nifty AAA Bond Plus SDL Apr 2026 50:50 Index",
    "AXISILVER.NS": "Axis Silver ETF",
    "GILT5YBEES.NS": "Nifty 5 yr Benchmark G-Sec Index",
    "GSEC10ABSL.NS": "CRISIL 10 Year Gilt ETF",
    "LICNETFGSC.NS": "GSEC10 NSE Index",
    "UNIONGOLD.NS": "Commodity Gold",
    "MODEFENCE.NS": "Nifty India Defence Total Return Index",
    "MON100.NS": "Nasdaq100",
    "GROWWGOLD.NS": "Commodity",
    "GOLD360.NS": "Commodity \uff96 Gold",
    "HDFCGOLD.NS": "Gold",
    "GOLDCASE.NS": "Zerodha Gold ETF",
    "AXISGOLD.NS": "Gold",
    "IVZINGOLD.NS": "Gold",
    "PHARMABEES.NS": "Nifty Pharma TRI",
    "HNGSNGBEES.NS": "Hang Seng Index",
    "GOLDETF.NS": "Mirae Asset Gold ETF",
    "MOGSEC.NS": "Nifty 5 yr Benchmark G-Sec Index",
    "GOLDIETF.NS": "Gold",
    "HDFCSILVER.NS": "HDFC Silver ETF",
    "GOLDBEES.NS": "Gold",
    "SETFGOLD.NS": "Gold",
    "QGOLDHALF.NS": "Gold",
    "SILVERIETF.NS": "Domestic Price of Silver",
    "SILVER1.NS": "Kotak Silver ETF",
    "GROWWRAIL.NS": "Nifty India Railways PSU Index",
    "BBNPPGOLD.NS": "Baroda BNP Paribas Gold ETF",
    "SILVER360.NS": "Commodity-Silver",
    "SILVERBEES.NS": "Domestic price of Silver- based on LBMA Silver daily spot fixing price",
    "SILVERCASE.NS": "Commodity-Silver",
    "TATSILV.NS": "Tata Silver Exchange Traded Fund",
    "SILVERETF.NS": "UTI Silver Exchange Traded Fund (UTI Silver ETF)",
    "SBISILVER.NS": "SBI SILVER ETF",
    "PVTBANKADD.NS": "DSP Nifty Private Bank ETF",
    "LICMFGOLD.NS": "Gold",
    "GOLDETFADD.NS": "DSP Gold ETF",
    "EGOLD.NS": "Edelweiss Gold ETF",
    "SILVER.NS": "Physical price of Silver",
    "ESILVER.NS": "Edelweiss Silver ETF",
    "SILVERADD.NS": "DSP Silver ETF",
    "SILVRETF.NS": "Mirae Asset Silver ETF",
    "LICNFNHGP.NS": "Nifty 100",
    "MID150.NS": "Nifty Midcap 150 Index",
    "LICNETFSEN.NS": "SENSEX",
    "UTISXN50.NS": "BSE Sensex Next 50",
    "EVIETF.NS": "Nifty EV & New Age Automotive ETF",
  

            # "PIDILITIND.NS": "PIDILITIND - Stocks",
            # "APOLLOPIPE.NS": "Apollo Pipes - Stocks",
            # "IRCTC.NS": "Irctc Stocks",
            # "MSUMI.NS": "Stocks",
            # "SONACOMS.NS": "Stocks",
            # "APTUS.NS": "Stocks",
            # "RRKABEL.NS": "Stocks",
            # "AAVAS.NS": "Stocks",
            # "AFFLE.NS": "Stocks",
            # "ANGELONE.NS": "Stocks",
            # "APTUS.NS": "Stocks",
            # "BAJFINANCE.NS": "Stocks",
            # "BERGEPAINT.NS": "Stocks",
            # "COFORGE.NS": "Stocks",
            # "DMART.NS": "Stocks",
            # "LTIM.NS": "Stocks",
            # "LTTS.NS": "Stocks",
            # "NAUKRI.NS": "Stocks",
            # "PIIND.NS": "Stocks",
            # "POLYCAB.NS": "Stocks",
            # "SRF.NS": "Stocks",
            # "TATAELXSI.NS": "Stocks",
            # "TITAN.NS": "Stocks",
            # "VBL.NS": "Stocks",
            # "IRFC.BO": "Stocks",
        }