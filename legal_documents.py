from typing import List, Optional

def generate_affidavit(
    petitioner: str,
    respondent: str,
    deponent_name: str,
    deponent_age: Optional[str] = "____ years",
    father_name: Optional[str] = "______",
    address: Optional[str] = "________________",
    petition_no: Optional[str] = "____",
    year: Optional[str] = "2000",
    place_verified: Optional[str] = "________",
    date_day: Optional[str] = "___",
    date_month: Optional[str] = "_________"
) -> str:
    """Generate a formal affidavit (Writ Petition)."""
    return f"""
IN THE HON'BLE HIGH COURT OF MADHYA PRADESH AT JABALPUR

WRIT PETITION NO. {petition_no} OF {year}

{petitioner}
VERSUS
{respondent}

Affidavit of {deponent_name}, aged about {deponent_age}, son/daughter of {father_name}, resident of {address}.

I, the deponent above-named, do hereby solemnly affirm and state on oath as under:

1. That I am the Petitioner in the aforesaid Writ Petition and am conversant with full facts of the case.

2. That the deponent has read the Writ Petition and annexures, the contents of which he/she has fully understood.

3. That the contents of paragraphs 1 to 20 of the Writ Petition are true to the own knowledge of the deponent.

4. That annexures A to T to the Writ Petition have been compared and are certified to be true copies of their originals.

DEPONENT: {deponent_name}

I, the above-named deponent, do verify that the contents of paragraphs 1 to 4 of this affidavit are true to my own knowledge. No part of it is false and nothing material has been concealed.

Verified at {place_verified}, on this {date_day} day of {date_month}, {year}.

DEPONENT: {deponent_name}
""".strip()


def generate_name_change_affidavit(
    deponent_name: str,
    maiden_name: str,
    husband_name: Optional[str],
    marriage_date: str,
    marriage_place: str,
    marriage_certificate_no: Optional[str],
    aadhar_number: Optional[str],
    pan_number: Optional[str],
    new_name: str,
    passport_photo_attached: bool = True
) -> str:
    """Affidavit for change of name after marriage (female)."""
    photo_note = "Affix Passport Size Photograph (attested by Notary)." if passport_photo_attached else "No photograph attached."
    return f"""
AFFIDAVIT FOR CHANGE OF NAME AFTER MARRIAGE [FEMALE]

I, {deponent_name}, daughter of ___________________________ and wife of {husband_name or '________________'}, aged _________, residing at ____________________________, do hereby solemnly affirm and declare as under:

1. That my maiden name is {maiden_name}.
2. That I got married to {husband_name or '__________'} on {marriage_date} at {marriage_place} vide marriage certificate number {marriage_certificate_no or '__________'} dated {marriage_date}.
3. After marriage my new name is {new_name}.
4. That in my marriage certificate both the names (maiden and present) are stated.
5. That my AADHAR number is {aadhar_number or '__________'} which is same before and after marriage.
6. That my PAN number is {pan_number or '__________'} which is same before and after marriage.
7. I state that {maiden_name} and {new_name} are the names of one and the same person (myself).
8. I am executing this declaration to be submitted to concerned authorities for change of my name in their records.

I hereby state that whatever is stated above is true to the best of my knowledge.

Signature of Deponent: {deponent_name}          Date: __________

{photo_note}

WITNESSES:
1) ________________________
2) ________________________

NOTES:
1. The affidavit has to be sworn before a Notary Public.
2. Attach copies of Aadhar Card, PAN Card, Marriage Certificate.
""".strip()


def generate_will(
    testator_name: str,
    relation_to_parent: Optional[str] = "son/daughter of Shri _______________",
    age: Optional[str] = "___ years",
    address: Optional[str] = "______________________________",
    executor_name: str = "________________",
    beneficiaries: Optional[List[str]] = None,
    assets: Optional[List[str]] = None,
    date_day: Optional[str] = "____",
    date_month: Optional[str] = "____",
    year: Optional[str] = "2000",
    place: Optional[str] = "__________",
    witnesses: Optional[List[str]] = None
) -> str:
    """Generate a simple last will and testament."""
    beneficiaries = beneficiaries or ["{beneficiary}"]
    assets = assets or ["Flat No.___ in ______________", "Jewelry", "Cash", "Bank Deposits"]
    witnesses = witnesses or ["1. __________________", "2. __________________"]

    assets_text = "\n".join(f"- {a}" for a in assets)
    beneficiaries_text = ", ".join(beneficiaries)
    witnesses_text = "\n".join(witnesses)

    return f"""
LAST WILL AND TESTAMENT

I, {testator_name}, {relation_to_parent}, aged {age}, resident of {address}, do hereby revoke all my former Wills and declare this to be my last Will and Testament.

I appoint {executor_name} as the sole Executor of this Will.

I declare that I own the following assets:
{assets_text}

I hereby give, devise and bequeath all my properties, whether movable or immovable, whatsoever and wheresoever to: {beneficiaries_text} absolutely and forever.

IN WITNESS WHEREOF I have hereunto set my hands on this {date_day} day of {date_month}, {year} at {place}.

Signed: {testator_name}

WITNESSES:
{witnesses_text}
""".strip()


def generate_power_of_attorney(
    grantor_name: str,
    agent_name: str,
    grantor_age: Optional[str] = "___ yrs",
    grantor_address: Optional[str] = "________________",
    property_description: Optional[str] = "the property at __________________",
    permissions: Optional[List[str]] = None,
    effective_date: Optional[str] = "________"
) -> str:
    """General power of attorney for property management."""
    permissions = permissions or [
        "rent the property and execute leave & license agreements",
        "collect rent and issue receipts",
        "manage repairs and obtain permissions",
        "pay taxes, municipal levies and society charges",
        "represent before courts/authorities and engage advocates"
    ]
    perms_text = "\n".join(f"{i+1}. {p}" for i, p in enumerate(permissions))

    return f"""
POWER OF ATTORNEY

TO ALL TO WHOM THESE PRESENTS SHALL COME:

Know all men by these presents that I {grantor_name}, s/o/d/o {grantor_age}, resident of {grantor_address}, do hereby nominate and appoint Shri/Smt {agent_name}, R/o _______________ as my true and lawful Attorney to act for and on my behalf in respect of {property_description} and to perform the following powers with effect from {effective_date}:

{perms_text}

Provided that the said attorney shall not sell or transfer ownership of the property without my prior written consent. The attorney shall keep true accounts of all activities performed by virtue of this power.

IN WITNESS WHEREOF I have executed this Power of Attorney on this day ______________.

EXECUTANT:
Name & Signature: {grantor_name}

ATTORNEY HOLDER:
Name & Signature: {agent_name}

WITNESSES:
1. __________________
2. __________________
""".strip()


def generate_special_power_of_attorney(
    grantor_name: str,
    agent_name: str,
    property_details: str,
    date_signed: Optional[str] = "________"
) -> str:
    """Special POA for executing sale deed and registration."""
    return f"""
SPECIAL POWER OF ATTORNEY TO EXECUTE SALE DEED

KNOW ALL MEN BY THESE PRESENTS that I, {grantor_name}, do hereby appoint {agent_name} as my true and lawful attorney to negotiate and execute the sale deed of the property described as: {property_details}.

The attorney is empowered to:
1. Negotiate sale terms and execute the sale deed.
2. Declare value for registration and present the deed before the Sub-Registrar.
3. Complete registration formalities and receive the registered document.

IN WITNESS WHEREOF I have signed this deed on {date_signed}.

EXECUTANT: {grantor_name}
ATTORNEY: {agent_name}

WITNESSES:
1. __________________
2. __________________
""".strip()


def vakalatnama(
    your_name: str,
    lawyer_name: str,
    court_name: Optional[str] = "Hon'ble Court",
    case_title: Optional[str] = "Suit/Appeal/Petition",
    role: Optional[str] = "Petitioner/Applicant",
    date: Optional[str] = "________",
    place: Optional[str] = "________"
) -> str:
    """Generate a vakalatnama (appointment of advocate)."""
    return f"""
VAKALATNAMA

Before the {court_name}

Between:
{case_title}   -  {role}

I/we {your_name} do hereby appoint and retain {lawyer_name} (hereinafter called "the Advocate") to be my/our advocate in the said matter and authorize the Advocate to represent, sign, file, present and receive all documents, to appear in court, to withdraw or compromise, to deposit and draw money, and to do all acts necessary in the matter.

Signatures of Person(s) Appointing the Advocate:
{your_name}

Advocate Name: {lawyer_name}
Enrollment No.: __________________
Mobile No.: _____________________
Signature of Advocate: __________________

Date: {date}
Place: {place}
""".strip()


def generate_tenancy_lease(
    lessor: str,
    lessee: str,
    property_address: str,
    rent_amount: str,
    duration_months: int,
    start_date: str,
    security_deposit: Optional[str] = None,
    notice_period_days: Optional[int] = 30
) -> str:
    """Simple monthly tenancy lease agreement."""
    security_text = f"Security deposit: Rs. {security_deposit}." if security_deposit else "No security deposit specified."
    return f"""
LEASE OF A HOUSE ON MONTHLY TENANCY

This Agreement of Lease is entered into on {start_date} between {lessor} (Lessor) and {lessee} (Lessee).

1. Property: {property_address}
2. Rent: Rs. {rent_amount} per month, payable in advance on or before the 1st day of each month.
3. Duration: {duration_months} months commencing {start_date}.
4. Security: {security_text}
5. Notice to vacate: {notice_period_days} days written notice.
6. Lessee shall keep premises in good condition; Lessor may inspect at reasonable times.
7. Lessee shall not sublet without written permission of Lessor.
8. Utilities: Lessee shall pay electricity and water charges unless otherwise agreed in writing.

IN WITNESS WHEREOF, the parties have signed this Lease on {start_date}.

Lessor: {lessor}       Lessee: {lessee}

WITNESSES:
1. __________________
2. __________________
""".strip()


# Example usage (run in your app)
if __name__ == "__main__":
    # Example: create an affidavit text
    affidavit = generate_affidavit(
        petitioner="John Doe",
        respondent="State of Madhya Pradesh",
        deponent_name="John Doe",
        deponent_age="45 years",
        father_name="Ravi Doe",
        address="12, Civil Lines, Jabalpur",
        petition_no="123",
        year="2025",
        place_verified="Jabalpur",
        date_day="19",
        date_month="November"
    )
    print(affidavit)
