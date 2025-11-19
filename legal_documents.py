# legal_documents_standard.py
"""
Standard Indian Legal Draft Format - Document Generator
Author: ChatGPT (reformatted into Option A: standard Indian legal draft style)
Usage: import functions and call with required parameters. Each generator returns a string.
Optional: save_as_docx(text, filename) requires python-docx (pip install python-docx).
"""

from typing import List, Optional
from datetime import date

def _center(text: str) -> str:
    return text.center(80)

def _line() -> str:
    return "_" * 80

def save_as_docx(text: str, filename: str):
    """
    Optional: write `text` to a simple .docx file.
    Requires: pip install python-docx
    """
    try:
        from docx import Document
        doc = Document()
        for line in text.splitlines():
            doc.add_paragraph(line)
        doc.save(filename)
    except Exception as e:
        raise RuntimeError("save_as_docx failed. Install python-docx and try again.") from e


def generate_affidavit(
    petitioner: str,
    respondent: str,
    petition_no: str,
    year: str,
    deponent_name: str,
    deponent_age: str,
    father_or_husband_name: str,
    address: str,
    paragraphs_true_up_to: int = 20,
    annexures_range: str = "A to T",
    place_verified: str = "__________",
    day: str = "___",
    month: str = "_________"
) -> str:
    """
    Generates an affidavit in standard Indian legal format for a writ petition.
    Returns a formatted string.
    """
    header = "\n".join([
        _center("IN THE HON'BLE HIGH COURT OF MADHYA PRADESH AT JABALPUR"),
        "",
        _center(f"WRIT PETITION NO. {petition_no} OF {year}"),
        "",
        _center(petitioner.upper()),
        _center("VERSUS"),
        _center(respondent.upper()),
        ""
    ])

    body = f"""
AFFIDAVIT

I, {deponent_name}, aged about {deponent_age}, son/daughter of {father_or_husband_name}, resident of {address}, do hereby solemnly affirm and state on oath as under:

1. That I am the Petitioner in the aforesaid Writ Petition and am conversant with the facts of the case and therefore competent to swear this affidavit.

2. That I have read the Writ Petition and the annexures thereto and I know the contents of the same and the contents thereof are true and correct.

3. That the contents of paragraphs 1 to {paragraphs_true_up_to} of the Writ Petition are true to my own knowledge and belief.

4. That annexures {annexures_range} to the Writ Petition are true copies of their respective originals and have been verified by me.

5. That no part of this affidavit is false and nothing material has been concealed therefrom.

DEPONENT:
Name: {deponent_name}
Signature: _______________________

VERIFICATION

Verified at {place_verified} on this {day} day of {month}, {year} that the contents of paragraphs 1 to 5 above are true to my own knowledge and belief and no part of it is false and nothing material has been concealed therefrom.

Signature of Deponent: _______________________
Name: {deponent_name}
Date: {day}/{month}/{year}
Place: {place_verified}
""".strip()

    footer = "\n\n" + _line() + "\n"
    return header + body + footer


def generate_name_change_affidavit(
    deponent_name: str,
    maiden_name: str,
    married_name: str,
    father_name: str,
    husband_name: Optional[str],
    marriage_date: str,
    marriage_place: str,
    marriage_certificate_no: Optional[str],
    aadhar_number: Optional[str],
    pan_number: Optional[str],
    photo_attested: bool = True
) -> str:
    """
    Affidavit for change of name after marriage (female) in standard format.
    """
    photo_note = "Passport size photograph affixed and attested by Notary." if photo_attested else "No photograph attached."

    header = _center("AFFIDAVIT FOR CHANGE OF NAME AFTER MARRIAGE") + "\n\n"

    body = f"""
I, {deponent_name}, daughter of {father_name} and wife of {husband_name or '__________'}, aged ____ years, residing at _____________________________, do hereby solemnly affirm and declare as under:

1. That my maiden name is: {maiden_name}.

2. That I got married to {husband_name or '__________'} on {marriage_date} at {marriage_place} and my marriage certificate number is {marriage_certificate_no or '__________'}.

3. That after marriage my name is changed to: {married_name}.

4. That my AADHAR number is: {aadhar_number or '__________'} and my PAN number is: {pan_number or '__________'}.

5. That {maiden_name} and {married_name} refer to one and the same person, that is, myself.

6. That I am executing this affidavit for the purpose of getting my name changed in the records of concerned authorities.

DEPONENT:
Name: {deponent_name}
Signature: _______________________

{photo_note}

WITNESSES:
1. Name: __________________   Signature: __________________
2. Name: __________________   Signature: __________________

VERIFICATION

Verified at __________ on this ___ day of ________, 20__ that the contents of this affidavit are true and correct to the best of my knowledge and belief.

Signature of Deponent: _______________________
Name: {deponent_name}
""".strip()

    return header + body


def generate_will(
    testator_name: str,
    relation: str,
    age: str,
    address: str,
    executor_name: str,
    beneficiaries: List[str],
    assets_list: Optional[List[str]] = None,
    date_day: str = "___",
    date_month: str = "________",
    year: str = "20__",
    place: str = "________"
) -> str:
    """
    Simple Last Will and Testament in standard court-friendly format.
    """
    assets_list = assets_list or [
        "One Flat No. ___ situated at ____________________________.",
        "Jewellery, ornaments and valuables.",
        "Bank balances, deposits, investments and securities."
    ]

    header = _center("LAST WILL AND TESTAMENT") + "\n\n"

    assets_text = "\n".join([f" - {a}" for a in assets_list])
    beneficiaries_text = "\n".join([f" - {b}" for b in beneficiaries])

    body = f"""
I, {testator_name}, {relation}, aged {age}, resident of {address}, revoke all former Wills and declare this to be my last Will and Testament.

1. I appoint {executor_name} as the Executor of this my Will.

2. I declare that I am of sound disposing mind and make this Will of my own free will and without undue influence.

3. I own the following assets:
{assets_text}

4. I hereby give, devise and bequeath all my movable and immovable property, whether present or future, whatsoever and wheresoever to the following person(s):

{beneficiaries_text}

5. All debts, funeral and testamentary expenses shall be paid out of my estate.

IN WITNESS WHEREOF I have set my hand this {date_day} day of {date_month}, {year} at {place}.

Signed by the above-named Testator: {testator_name}
Signature: _______________________

WITNESSES:
1. Name: __________________  Address: __________________  Signature: __________________
2. Name: __________________  Address: __________________  Signature: __________________
""".strip()

    return header + body


def generate_power_of_attorney(
    grantor_name: str,
    grantor_address: str,
    agent_name: str,
    agent_address: str,
    scope_of_powers: List[str],
    not_allowed: Optional[str] = "The attorney shall not sell or transfer ownership of the property without prior written consent of the grantor.",
    date_signed: str = "________"
) -> str:
    """
    General Power of Attorney in standard format for property/management.
    """
    header = _center("POWER OF ATTORNEY") + "\n\n"

    powers_text = "\n".join([f"{i+1}. {p}" for i, p in enumerate(scope_of_powers)])

    body = f"""
KNOW ALL MEN BY THESE PRESENTS that I, {grantor_name}, residing at {grantor_address}, do hereby appoint {agent_name}, residing at {agent_address}, to be my true and lawful Attorney to do the following acts, deeds and things on my behalf:

{powers_text}

{not_allowed}

This Power of Attorney is executed voluntarily on this day {date_signed}.

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
""".strip()

    return header + body


def generate_special_power_of_attorney(
    grantor_name: str,
    grantor_address: str,
    agent_name: str,
    property_description: str,
    date_signed: str = "________"
) -> str:
    """
    Special Power of Attorney for executing sale deed and registration.
    """
    header = _center("SPECIAL POWER OF ATTORNEY TO EXECUTE SALE DEED AND PRESENT FOR REGISTRATION") + "\n\n"

    body = f"""
KNOW ALL MEN BY THESE PRESENTS that I, {grantor_name} of {grantor_address}, do hereby appoint {agent_name} to be my true and lawful Attorney for the specific purpose of negotiating, executing and presenting for registration the Sale Deed in respect of the property described as follows:

PROPERTY DESCRIPTION:
{property_description}

POWERS:
1. To negotiate terms and execute the Sale Deed and ancillary documents.
2. To present the Sale Deed before the Sub-Registrar and to declare the consideration for registration.
3. To pay stamp duty, registration fees and to sign receipts and obtain the registered document.
4. To do all acts and things necessary for the completion of the sale and registration.

IN WITNESS WHEREOF I have executed this Special Power of Attorney on this day {date_signed}.

EXECUTANT:
Name: {grantor_name}
Signature: _______________________
Address: {grantor_address}

ATTORNEY:
Name: {agent_name}
Signature: _______________________
Address: _______________________

WITNESSES:
1. Name: __________________  Signature: __________________  Address: __________________
2. Name: __________________  Signature: __________________  Address: __________________
""".strip()

    return header + body


def generate_vakalatnama(
    principal_name: str,
    advocate_name: str,
    court_name: str,
    case_title: str,
    enrolment_no: Optional[str] = None,
    date_signed: str = "________"
) -> str:
    """
    Vakalatnama (appointment of advocate) in standard format.
    """
    header = _center("VAKALATNAMA") + "\n\n"

    body = f"""
BEFORE THE {court_name.upper()}

Between:
{case_title}

I/We, {principal_name}, do hereby appoint and retain {advocate_name} (Enrollment No.: {enrolment_no or '________'}) to be my/our advocate in the above matter and to do all acts, deeds and things necessary in relation thereto including signing and filing of documents, representation before the Court, receiving documents, compromises and withdrawals.

Signature of Principal: _______________________
Name: {principal_name}

Advocate:
Name: {advocate_name}
Enrollment No.: {enrolment_no or '__________'}
Signature: _______________________

Date: {date_signed}
Place: _______________________
""".strip()

    return header + body


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
    """
    Lease of house on monthly tenancy in standard legal format.
    """
    header = _center("LEASE OF A HOUSE ON MONTHLY TENANCY") + "\n\n"

    security_text = f"Security deposit: Rs. {security_deposit_in_rs}." if security_deposit_in_rs else "Security deposit: Not specified."

    body = f"""
THIS AGREEMENT OF LEASE is made on this {lease_commencement_date} between:

LESSOR: {lessor_name}, residing at {lessor_address} (hereinafter called the 'Lessor');

AND

LESSEE: {lessee_name}, residing at {lessee_address} (hereinafter called the 'Lessee').

1. The Lessor lets and the Lessee takes on lease the house/property known as: {property_address}.

2. TERM: The lease shall commence on {lease_commencement_date} for a period of {lease_duration_months} months.

3. RENT: The rent shall be Rs. {rent_amount_in_rs} per month payable in advance on or before the 1st day of each month.

4. SECURITY: {security_text}

5. USE: The Lessee shall use the premises only for residential purposes and shall not sublet the premises without the written consent of the Lessor.

6. MAINTENANCE & REPAIRS: The Lessee shall keep the premises in good condition. Structural repairs shall be the responsibility of the Lessor.

7. UTILITIES: The Lessee shall pay electricity and water charges and other utilities unless otherwise agreed in writing.

8. TERMINATION: Either party may terminate by giving {notice_period_days} days written notice to the other party.

9. POSSESSION: The Lessee shall deliver peaceful and vacant possession at the end of the lease term.

IN WITNESS WHEREOF the parties hereto have set their hands on this {lease_commencement_date}.

LESSOR: {lessor_name}            LESSEE: {lessee_name}
Signature: __________________     Signature: __________________

WITNESSES:
1. Name: __________________  Signature: __________________  Address: __________________
2. Name: __________________  Signature: __________________  Address: __________________
""".strip()

    return header + body


# ---------- Example usage ----------
if __name__ == "__main__":
    # Example: affidavit
    affidavit_text = generate_affidavit(
        petitioner="John Doe",
        respondent="State of Madhya Pradesh",
        petition_no="123/2025",
        year="2025",
        deponent_name="John Doe",
        deponent_age="45 years",
        father_or_husband_name="Ravi Doe",
        address="12, Civil Lines, Jabalpur",
        place_verified="Jabalpur",
        day="19",
        month="November"
    )
    print(affidavit_text)

    # Save as docx (uncomment to use; requires python-docx)
    # save_as_docx(affidavit_text, "affidavit.docx")
