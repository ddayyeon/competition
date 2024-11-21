import streamlit as st

# 유형별 정보
investment_types = {
    "1유형 : 김혜수 (타짜)": "투자 성향 요약: 매우 높은 위험을 감수할 수 있으며, 높은 수익 기대치를 가지고 단기 투자를 선호. 중소기업을 선호하고, 자본 이득을 중시하며 집중 투자를 선호하는 성향.\n\n추천 종목:\n1. 기업명: 카카오게임즈\n   - 산업군: 게임 산업, 디지털 콘텐츠\n   - 최근 3년 투자 실적:\n     2021: 매출 2.4조 원, 영업이익 1.1조 원\n     2022: 매출 2.7조 원, 영업이익 1.4조 원\n     2023: 매출 3.0조 원, 영업이익 1.7조 원\n   - 최근 주가 성장률: 2021~2022: +45%, 2022~2023: +30%\n   - 배당금 지급 여부: 없음\n\n2. 기업명: 테슬라\n   - 산업군: 전기차, 기술 혁신\n   - 최근 3년 투자 실적:\n     2021: 매출 53.8조 원, 영업이익 5.6조 원\n     2022: 매출 70.8조 원, 영업이익 6.2조 원\n     2023: 매출 90.2조 원, 영업이익 7.5조 원\n   - 최근 주가 성장률: 2021~2022: +70%, 2022~2023: +40%\n   - 배당금 지급 여부: 없음\n\n종합 평가:\n이 포트폴리오는 게임 산업과 전기차 산업의 핵심 기업인 카카오게임즈와 테슬라를 중심으로 구성되어 있습니다.\n카카오는 모바일 게임 및 메타버스 콘텐츠를 통해 고속 성장을 이어가고 있으며, 테슬라는 전기차와 혁신적인 기술 분야에서 탁월한 성장 가능성을 보이고 있습니다.\n두 기업 모두 배당금 지급은 하지 않지만, 주식의 큰 성장 잠재력과 리스크를 감안한 투자가 필요합니다.\n이 포트폴리오는 단기적인 자본 이득을 추구하는 투자자에게 적합하며, 고위험 고수익의 전략을 취할 수 있는 기업들입니다.\n빠르게 변화하는 산업 트렌드를 잘 반영하고 있으며, 위험을 감수할 수 있는 투자자에게 매력적인 선택이 될 것입니다.",
    "4유형 : 손예진 (사랑의 불시착)": "투자 성향 요약: 안정적인 수익을 선호하면서도 높은 수익률을 기대하는 투자자. 장기 투자와 배당 수익을 중시하며, 대기업 및 분산 투자를 지향함.\n\n추천 종목:\n1. 기업명: 삼성전자\n   - 산업군: 반도체 및 전자제품\n   - 최근 3년 투자 실적:\n     2021: 매출 279조 원, 영업이익 51조 원\n     2022: 매출 302조 원, 영업이익 43조 원\n     2023: 매출 307조 원, 영업이익 48조 원\n   - 최근 주가 성장률: 2021~2022: +30%, 2022~2023: +40%\n   - 배당금 지급 여부: 지급 (2023년 기준 배당 수익률 2.5%)\n\n2. 기업명: SK하이닉스\n   - 산업군: 메모리 반도체\n   - 최근 3년 투자 실적:\n     2021: 매출 43조 원, 영업이익 12조 원\n     2022: 매출 44조 원, 영업이익 9조 원\n     2023: 매출 48조 원, 영업이익 10조 원\n   - 최근 주가 성장률: 2021~2022: +20%, 2022~2023: +25%\n   - 배당금 지급 여부: 지급 (2023년 기준 배당 수익률 1.8%)\n\n종합 평가:\n이 포트폴리오는 글로벌 반도체 시장의 핵심 기업인 삼성전자와 SK하이닉스를 포함하고 있어 안정적인 수익과 배당을 동시에 추구할 수 있습니다.\n삼성전자는 반도체 산업의 글로벌 리더로, 안정적인 실적과 배당 수익(2.5%)을 제공하며, 기술 혁신을 통해 장기적인 성장을 지속하고 있습니다.\nSK하이닉스는 데이터센터와 AI 산업 성장의 수혜를 받는 메모리 반도체 분야의 강자로, 꾸준한 매출 증가와 더불어 소폭의 배당 수익(1.8%)도 제공합니다.\n이 포트폴리오는 장기 투자자에게 적합하며, 안정적인 배당 수익과 성장 잠재력을 모두 충족합니다.\n분산 투자를 통해 위험을 최소화하면서도 기대 수익을 높일 수 있습니다.\n두 기업 모두 반도체 산업의 글로벌 리더로서, 산업의 변화에 따라 장기적인 성장 가능성이 큽니다.",
    "6유형 : 아이유 (호텔 델루나)": "투자 성향 요약: 안정적 투자 선호, 안정적인 수익을 추구하며, 배당금 수익을 중시하고 장기 투자를 선호. 대기업을 선호하며, 분산 투자로 위험을 최소화하고 안정적인 수익을 추구하는 성향.\n\n추천 종목:\n1. 기업명: LG화학\n   - 산업군: 화학, 전지 산업\n   - 최근 3년 투자 실적:\n     2021: 매출 37조 원, 영업이익 3.5조 원\n     2022: 매출 42조 원, 영업이익 4.2조 원\n     2023: 매출 45조 원, 영업이익 4.5조 원\n   - 최근 주가 성장률: 2021~2022: +12%, 2022~2023: +15%\n   - 배당금 지급 여부: 지급 (2023년 기준 배당 수익률 3.3%)\n\n2. 기업명: 삼성생명\n   - 산업군: 금융, 보험\n   - 최근 3년 투자 실적:\n     2021: 매출 25조 원, 영업이익 2.8조 원\n     2022: 매출 27조 원, 영업이익 3.1조 원\n     2023: 매출 28조 원, 영업이익 3.3조 원\n   - 최근 주가 성장률: 2021~2022: +5%, 2022~2023: +8%\n   - 배당금 지급 여부: 지급 (2023년 기준 배당 수익률 4.0%)\n\n종합 평가:\n이 포트폴리오는 대기업 중심의 안정적인 투자로 구성되어 있으며, LG화학과 삼성생명은 각각 화학 및 전지 산업, 보험 산업에서 강력한 시장 위치를 차지하고 있습니다.\nLG화학은 친환경 기술과 전기차 배터리 산업에서 성장 가능성을 보이며, 안정적인 배당 수익(3.3%)을 제공합니다.\n삼성생명은 높은 배당 수익률(4.0%)과 안정적인 수익을 통해 리스크가 적고 안정적인 수익을 추구하는 투자자에게 적합한 선택입니다.\n이 포트폴리오는 매우 낮은 위험을 선호하는 투자자에게 적합하며, 안정적인 수익과 배당 수익을 중시합니다.\n분산 투자를 통해 위험을 최소화하고, 안정적이고 지속적인 수익을 추구할 수 있습니다.\n이 포트폴리오는 장기 투자에 적합하며, 시장 변동성에 민감하지 않으며, 안정성을 중시하는 투자자에게 매력적인 선택입니다."
}

# Streamlit 앱 시작
st.title('주식 종목 추천 시스템')

# 투자 유형 선택
selected_type = st.selectbox('투자 유형을 선택하세요:', list(investment_types.keys()))

# 선택된 유형의 정보 출력
type_info = investment_types[selected_type]

# Streamlit에서 텍스트를 여러 열로 나누어 출력
type_lines = type_info.split('\n')
for line in type_lines:
    st.text(line)
    
 
import os
import openai
import streamlit as st

# OpenAI API 키 설정 (사용자 키로 대체)
openai.api_key = "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"

# 시장별 종목 번호 데이터
kospi_60 = ['005930.KS', '000660.KQ', '035420.KQ', '051910.KQ', '005380.KS', '012330.KS', '003550.KS', '068270.KQ', '017670.KS', '003670.KS',
            '009150.KS', '086790.KQ', '034730.KQ', '036570.KQ', '018250.KS', '030200.KQ', '004020.KS', '010950.KS', '009830.KS', '024110.KS',
            '018880.KS', '028050.KQ', '006400.KS', '004440.KS', '003490.KS', '001120.KS', '008770.KS', '005490.KS', '016360.KS', '015760.KS',
            '011200.KS', '011780.KS', '006260.KS', '027410.KQ', '030350.KQ', '004170.KS', '016610.KS', '002380.KS', '010140.KS', '005610.KS',
            '010130.KS', '086370.KQ', '003720.KS', '009830.KS', '010120.KQ', '009540.KQ', '000150.KS', '068270.KQ',
            '051900.KS', '007070.KS', '035250.KS', '003530.KS', '009240.KS', '001800.KS', '001360.KS', '001620.KS', '001680.KS']

kosdaq_60 = ['065170.KQ', '035720.KQ', '090430.KQ', '208340.KQ', '066570.KQ', '012750.KQ', '122990.KQ', '033780.KQ',
             '049770.KQ', '019680.KQ', '032640.KQ', '043650.KQ', '035760.KQ', '023530.KQ', '070300.KQ', '032540.KQ',
             '071050.KQ', '060370.KQ', '097950.KQ', '095720.KQ', '065530.KQ', '090350.KQ', '013700.KQ', '000150.KQ',
             '010420.KQ', '004000.KQ', '014820.KQ', '039490.KQ', '064260.KQ', '078350.KQ', '005850.KQ', '030520.KQ',
             '026960.KQ', '039420.KQ', '067160.KQ', '005190.KQ', '000270.KQ', '014830.KQ', '000120.KQ', '019170.KQ',
             '085310.KQ', '040300.KQ', '030610.KQ', '020560.KQ', '008600.KQ', '038540.KQ', '011390.KQ', '041960.KQ', '024110.KQ', '008470.KQ']

nasdaq_60 = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA', 'NVDA', 'META', 'PYPL', 'AMD', 'NFLX', 'INTC', 'CSCO', 'NFLX', 'INTU', 'BABA',
             'GOOG', 'AMZN', 'MSFT', 'VZ', 'MRNA', 'ROKU', 'BA', 'QS', 'ZM', 'CRWD', 'TME', 'ADBE', 'NOW', 'DOCU', 'SQ',
             'STZ', 'PANW', 'ETSY', 'DLR', 'PYPL', 'RBLX', 'UBER', 'SPOT', 'SNAP', 'EXPE', 'NVDA', 'AMZN', 'GOOG', 'TSLA',
             'META', 'NFLX', 'CSCO', 'INTC', 'PYPL', 'PYPL', 'SPOT', 'WMT', 'MSFT', 'ROKU', 'SQ', 'AAPL', 'V', 'TMO', 'MMM',
             'GS', 'MSFT', 'BA']

amex_60 = ['SPY', 'VOO', 'IWM', 'VTI', 'GDX', 'GLD', 'XLF', 'XLY', 'XLI', 'XLE', 'XLP', 'XLB', 'XLV', 'XLC', 'VOE', 'ITOT', 'VTV', 'VUG', 'SCHB',
           'SCHA', 'SCHX', 'SCHD', 'IWB', 'IWC', 'IWS', 'SPLV', 'VYM', 'SCHY', 'VGIT', 'VGLT', 'IGIB', 'BND', 'BNDX', 'AGG', 'USIG', 'BIL', 'VCSH',
           'GVI', 'HYD', 'TLT', 'IEF', 'SHY', 'SHV', 'MBB', 'LQD', 'SHV', 'JNK', 'LQD', 'ISTB', 'VTI', 'VOO', 'SPY', 'IWM', 'XLY', 'XLF']

nyse_60 = ['BA', 'DIS', 'KO', 'IBM', 'PFE', 'T', 'CAT', 'GE', 'JNJ', 'GS', 'XOM', 'AMGN', 'CVX', 'MMM', 'MCD', 'NKE', 'INTC', 'UNH', 'V', 'WMT',
           'VZ', 'NEE', 'PG', 'MSFT', 'DUK', 'HD', 'RTX', 'LMT', 'PYPL', 'MA', 'COST', 'ORCL', 'MCHP', 'HON', 'UPS', 'MO', 'ABT', 'PEP', 'LLY',
           'C', 'BLK', 'AMT', 'SCHW', 'TMO', 'MDT', 'XEL', 'TXN', 'RMD', 'AXP', 'EMR', 'QCOM', 'SPG', 'SYF', 'PSX', 'TSLA', 'AVGO', 'SLB', 'DHR']

# 선택 가능한 시장
market_options = {
    "KOSPI": kospi_60,
    "KOSDAQ": kosdaq_60,
    "NASDAQ": nasdaq_60,
    "AMEX": amex_60,
    "NYSE": nyse_60
}

# Streamlit 앱 구성
st.title("종목 번호 선택 및 기업 설명")

# 시장 선택
selected_market = st.selectbox("시장 선택:", list(market_options.keys()))

# 종목 번호 선택 (최대 5개 선택 가능)
selected_stocks = st.multiselect(
    "종목 번호를 선택하세요 (최대 5개):",
    market_options[selected_market],
    max_selections=5
)

# OpenAI를 활용한 기업 설명 생성 함수
def get_company_info(stock_numbers):
    descriptions = {}
    for stock in stock_numbers:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"주식 종목 번호 {stock}에 대해 간단히 설명해주세요."}
                ],
                max_tokens=100
            )
            descriptions[stock] = response.choices[0].message.content.strip()
        except Exception as e:
            descriptions[stock] = f"오류 발생: {e}"
    return descriptions

# 선택된 종목 번호에 대한 설명 출력
if selected_stocks:
    st.write(f"선택된 종목 번호: **{', '.join(selected_stocks)}**")
    st.subheader("기업 설명")
    company_info = get_company_info(selected_stocks)
    for stock, description in company_info.items():
        st.write(f"**{stock}:** {description}")
else:
    st.write("아직 종목 번호를 선택하지 않았습니다.")
    
