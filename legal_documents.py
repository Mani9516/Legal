# legal_documents_all.py
"""
Legal document generators — Standard Indian Legal Draft Format (Option A)
Provides functions that return formatted strings for:
- Writ Affidavit
- Name-change Affidavit (after marriage)
- Last Will & Testament
- General Power of Attorney (GPA)
- Special Power of Attorney (SPA)
- Vakalatnama
- Tenancy Lease Agreement

All fields are function parameters (no blanks). Optional helper: save_as_docx(text, filename).
"""

from typing import List, Optional


# ----------------- Helpers -----------------
def _center(text: str, width: int = 80) -> str:
    return text.center(width)


def _line(width: int = 80) -> str:
    return "_" * width


def save_as_docx(text: str, filename: str):
    """
    Save plain text to a .docx file (simple, line-by-line).
    Requires: pip install python-docx
    """
    try:
        from docx import Document
    except Exception as e:
        raise RuntimeError("python-docx is required for save_as_docx. Install with `pip install python-docx`.") from e

    doc = Document()
    for line in text.splitlines():
        doc.add_paragraph(line)
    doc.save(filename)


# ----------------- 1. Writ Affidavit -----------------
def generate_affidavit(
    court_name: str,
    court_place: str,
    petition_no: str,
    year: str,
    petitioner: str,
    respondent: str,
    deponent_name: str,
    deponent_age: str,
    father_or_husband_name: str,
    residence: str,
    paragraphs_true_up_to: int = 20,
    annexures_range: str = "A to T",
    verification_place: str = "",
    verification_day: str = "",
    verification_month: str = "",
) -> str:
    header = "\n".join([
        _center(f"IN THE HON'BLE HIGH COURT OF {court_name.upper()} AT {court_place.upper()}"),
        "",
        _center(f"WRIT PETITION NO. {petition_no} OF {year}"),
        ""
    ])

    parties = f"{petitioner}\n    ...Petitioner\nVs.\n{respondent}\n    ...Respondent\n\n"

    body = f"""AFFIDAVIT OF DEPONENT

Affidavit of {deponent_name}, aged about {deponent_age} years, son/daughter of {father_or_husband_name}, resident of {residence}.

I, {deponent_name}, the deponent above-named, do hereby solemnly affirm and state on oath as under:

1. That I am the Petitioner in the aforesaid Writ Petition and I am fully conversant with the facts of the case.

2. That I have read the Writ Petition and the annexures thereto and I fully understand the contents thereof.

3. That the contents of paragraphs 1 to {paragraphs_true_up_to} of the Writ Petition are true to my own knowledge and belief.

4. That annexures {annexures_range} to the Writ Petition have been compared by me with their respective originals and are certified to be true copies.

5. That no part of this affidavit is false and nothing material has been concealed therefrom.

DEPONENT
Name: {deponent_name}
Signature: _______________________

VERIFICATION

I, {deponent_name}, the above-named deponent, do hereby verify that the contents of paragraphs 1 to 5 of this affidavit are true to my personal knowledge and belief and nothing material has been concealed.

Verified at {verification_place} on this {verification_day} day of {verification_month}, {year}.

Signature of Deponent: _______________________
Name: {deponent_name}
"""

    return header + parties + body


# ----------------- 2. Name Change Affidavit -----------------
def generate_name_change_affidavit(
    deponent_name: str,
    father_name: str,
    husband_name: Optional[str],
    age: str,
    residence: str,
    maiden_name: str,
    present_name: str,
    marriage_date: str,
    marriage_place: str,
    marriage_certificate_no: Optional[str],
    aadhar_number: Optional[str],
    pan_number: Optional[str],
    witnesses: Optional[List[dict]] = None,
) -> str:
    witnesses = witnesses or [{"name": "________________", "address": "________________"} , {"name": "________________", "address": "________________"}]
    header = _center("AFFIDAVIT FOR CHANGE OF NAME AFTER MARRIAGE") + "\n\n"

    witness_text = ""
    for i, w in enumerate(witnesses, start=1):
        witness_text += f"{i}. Name: {w.get('name')}   Address: {w.get('address')}   Signature: __________________\n"

    body = f"""I, {deponent_name}, daughter of {father_name}, and wife of {husband_name or 'N/A'}, aged {age} years, residing at {residence}, do hereby solemnly affirm and declare as under:

1. That my maiden name is: {maiden_name}.

2. That I got married to {husband_name or 'N/A'} on {marriage_date} at {marriage_place}, and my Marriage Certificate number is {marriage_certificate_no or 'N/A'}.

3. That after my marriage, my name is changed to: {present_name}.

4. That my AADHAAR Number is: {aadhar_number or 'N/A'}.

5. That my PAN Number is: {pan_number or 'N/A'}.

6. That the names {maiden_name} and {present_name} refer to one and the same person (myself).

7. That I am executing this affidavit to be produced before the concerned authorities for the purpose of changing/updating my name in their records.

DEPONENT:
Name: {deponent_name}
Signature: _______________________

( Affix passport size photograph & get it attested by Notary )

WITNESSES:
{witness_text}

VERIFICATION

Verified at {residence.split(',')[0] if ',' in residence else residence} on this ___ day of ____________, 20__ that the contents of this affidavit are true and correct to my knowledge and belief.

Signature of Deponent: _______________________
Name: {deponent_name}
"""
    return header + body


# ----------------- 3. Will -----------------
def generate_will(
    testator_name: str,
    relation_to_parent: str,
    age: str,
    residence: str,
    executor_name: str,
    beneficiaries: List[dict],
    assets: Optional[List[str]] = None,
    date_day: str = "___",
    date_month: str = "________",
    year: str = "20__",
    place: str = "________"
) -> str:
    assets = assets or [
        "One Flat No. ___ situated at ____________________________.",
        "Jewellery and ornaments.",
        "Bank balances, deposits and investments."
    ]
    beneficiaries_text = "\n".join([f" - {b['name']} (Relationship: {b.get('relation','')})" for b in beneficiaries])
    assets_text = "\n".join([f" - {a}" for a in assets])

    header = _center("LAST WILL AND TESTAMENT") + "\n\n"

    body = f"""I, {testator_name}, {relation_to_parent}, aged {age}, residing at {residence}, hereby revoke all former Wills and declare this to be my last Will and Testament.

1. I appoint {executor_name} as the Executor of this my Will.

2. I declare that I am of sound mind and make this Will of my own free will.

3. My assets are as follows:
{assets_text}

4. I hereby give, devise and bequeath all my assets described above to the following beneficiary(ies):
{beneficiaries_text}

5. All debts, funeral and testamentary expenses shall be paid out of my estate.

IN WITNESS WHEREOF I have set my hand this {date_day} day of {date_month}, {year} at {place}.

Signed: {testator_name}
Signature: _______________________

WITNESSES:
1. Name: __________________  Address: __________________  Signature: __________________
2. Name: __________________  Address: __________________  Signature: __________________
"""
    return header + body


# ----------------- 4. General Power of Attorney -----------------
def generate_power_of_attorney(
    grantor_name: str,
    grantor_address: str,
    agent_name: str,
    agent_address: str,
    scope_of_powers: List[str],
    not_allowed_clause: Optional[str] = None,
    date_signed: str = "________"
) -> str:
    header = _center("POWER OF ATTORNEY") + "\n\n"
    powers_text = "\n".join([f"{i+1}. {p}" for i, p in enumerate(scope_of_powers)])
    not_allowed = not_allowed_clause or "The attorney shall not sell or transfer the ownership of the property without the prior written consent of the Grantor."

    body = f"""KNOW ALL MEN BY THESE PRESENTS that I, {grantor_name}, resident of {grantor_address}, do hereby nominate and appoint {agent_name}, resident of {agent_address}, to be my true and lawful Attorney to do the following acts, deeds and things on my behalf:

{powers_text}

{not_allowed}

This Power of Attorney is executed voluntarily on this day {date_signed}.

EXECUTANT:
Name: {grantor_name}
Signature: _______________________

ATTORNEY:
Name: {agent_name}
Signature: _______________________

WITNESSES:
1. Name: __________________  Signature: __________________  Address: __________________
2. Name: __________________  Signature: __________________  Address: __________________
"""
    return header + body


# ----------------- 5. Special Power of Attorney -----------------
def generate_special_power_of_attorney(
    grantor_name: str,
    grantor_address: str,
    agent_name: str,
    agent_address: str,
    property_description: str,
    specific_powers: Optional[List[str]] = None,
    date_signed: str = "________"
) -> str:
    header = _center("SPECIAL POWER OF ATTORNEY TO EXECUTE SALE DEED AND PRESENT FOR REGISTRATION") + "\n\n"
    specific_powers = specific_powers or [
        "To negotiate terms and execute the Sale Deed.",
        "To present the Sale Deed before the Sub-Registrar for registration.",
        "To declare the consideration and pay stamp duty and registration fees.",
        "To obtain the registered document and sign all receipts."
    ]
    powers_text = "\n".join([f"{i+1}. {p}" for i, p in enumerate(specific_powers)])

    body = f"""KNOW ALL MEN BY THESE PRESENTS that I, {grantor_name}, of {grantor_address}, do hereby appoint {agent_name}, of {agent_address}, to be my true and lawful attorney for the specific purpose of executing the sale deed and completing registration formalities in respect of the property described below:

PROPERTY DESCRIPTION:
{property_description}

POWERS:
{powers_text}

IN WITNESS WHEREOF I have signed this Special Power of Attorney on this day {date_signed}.

EXECUTANT:
Name: {grantor_name}
Signature: _______________________
Address: {grantor_address}

ATTORNEY:
Name: {agent_name}
Signature: _______________________
Address: {agent_address}

WITNESSES:
1. Name: __________________  Signature: __________________  Address: __________________
2. Name: __________________  Signature: __________________  Address: __________________
"""
    return header + body


# ----------------- 6. Vakalatnama -----------------
def generate_vakalatnama(
    principal_name: str,
    advocate_name: str,
    court_name: str,
    case_title: str,
    role: str,
    enrolment_no: Optional[str] = None,
    date_signed: str = "________",
    place: str = "________"
) -> str:
    header = _center("VAKALATNAMA") + "\n\n"

    body = f"""BEFORE THE {court_name.upper()}

Case / Matter: {case_title}
Role: {role}

I/We, {principal_name}, do hereby appoint and retain {advocate_name} (Enrollment No.: {enrolment_no or 'N/A'}) to be my/our Advocate in the above matter and authorize the Advocate to appear, represent, sign, file, verify, withdraw, compromise and do all acts necessary in relation thereto.

Signature of Principal: _______________________
Name: {principal_name}

Advocate:
Name: {advocate_name}
Enrollment No.: {enrolment_no or 'N/A'}
Signature: _______________________

Date: {date_signed}
Place: {place}
"""
    return header + body


# ----------------- 7. Tenancy Lease Agreement -----------------
def generate_tenancy_lease(
    lessor_name: str,
    lessor_address: str,
    lessee_name: str,
    lessee_address: str,
    property_address: str,
    rent_amount_in_rs: str,
    lease_commencement_date: str,
    lease_duration_months: int,
    security_deposit_in_rs: Optional[str] = None,
    notice_period_days: int = 30
) -> str:
    header = _center("LEASE OF A HOUSE ON MONTHLY TENANCY") + "\n\n"
    security_text = f"Security deposit: Rs. {security_deposit_in_rs}." if security_deposit_in_rs else "Security deposit: Not specified."

    body = f"""THIS AGREEMENT OF LEASE is made on this {lease_commencement_date} between:

LESSOR: {lessor_name}, residing at {lessor_address} (hereinafter called the 'Lessor');

AND

LESSEE: {lessee_name}, residing at {lessee_address} (hereinafter called the 'Lessee').

1. PROPERTY: The Lessor lets and the Lessee takes on lease the house/property known as: {property_address}.

2. TERM: The lease shall commence on {lease_commencement_date} for a period of {lease_duration_months} months.

3. RENT: The rent shall be Rs. {rent_amount_in_rs} per month payable in advance on or before the 1st day of each month.

4. SECURITY: {security_text}

5. USE: The Lessee shall use the premises for residential purposes only and shall not sublet the premises without the written consent of the Lessor.

6. MAINTENANCE & REPAIRS: The Lessee shall keep the premises in good repair. Structural repairs shall be the responsibility of the Lessor.

7. UTILITIES: The Lessee shall pay electricity, water and other utilities unless otherwise agreed in writing.

8. TERMINATION: Either party may terminate by giving {notice_period_days} days written notice to the other party.

9. POSSESSION: The Lessee shall deliver peaceful and vacant possession upon termination.

IN WITNESS WHEREOF the parties have executed this Lease on {lease_commencement_date}.

LESSOR: {lessor_name}            LESSEE: {lessee_name}
Signature: __________________     Signature: __________________

WITNESSES:
1. Name: __________________  Signature: __________________  Address: __________________
2. Name: __________________  Signature: __________________  Address: __________________
"""
    return header + body


# ----------------- Example usage -----------------
if __name__ == "__main__":
    # 1. Affidavit
    affidavit_text = generate_affidavit(
        court_name="Madhya Pradesh",
        court_place="Jabalpur",
        petition_no="123/2025",
        year="2025",
        petitioner="Mani Chourasiya",
        respondent="State of Madhya Pradesh",
        deponent_name="Mani Chourasiya",
        deponent_age="28 years",
        father_or_husband_name="Ramesh Chourasiya",
        residence="24, Shanti Nagar, Indore, Madhya Pradesh",
        verification_place="Indore",
        verification_day="19",
        verification_month="November"
    )
    print("--- AFFIDAVIT ---\n", affidavit_text[:800], "\n\n")

    # 2. Name change affidavit
    name_change = generate_name_change_affidavit(
        deponent_name="Priya Sharma",
        father_name="Rajesh Sharma",
        husband_name="Amit Singh",
        age="28",
        residence="12, Civil Lines, Jabalpur, MP",
        maiden_name="Priya Sharma",
        present_name="Priya Singh",
        marriage_date="12-02-2020",
        marriage_place="Indore",
        marriage_certificate_no="MC/2020/456",
        aadhar_number="123456789012",
        pan_number="ABCDE1234F"
    )
    print("--- NAME CHANGE AFFIDAVIT ---\n", name_change[:800], "\n\n")

    # 3. Will
    will_text = generate_will(
        testator_name="Rita Verma",
        relation_to_parent="daughter of Shri K.L. Verma",
        age="55",
        residence="45, Green Park, Bhopal",
        executor_name="Sunil Verma",
        beneficiaries=[{"name":"Sunil Verma","relation":"Son"}, {"name":"Meera Verma","relation":"Daughter"}],
        assets=["Flat No. 12, Blue Apartments, Bhopal", "Savings in SBI: Rs. 2,00,000"]
    )
    print("--- WILL ---\n", will_text[:800], "\n\n")
