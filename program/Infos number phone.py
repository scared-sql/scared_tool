import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberType
from colorama import Fore, Style, init

init(autoreset=True)

BRIGHT_GREEN = "\033[38;2;0;255;0m"
BRIGHT_BLUE = "\033[38;2;0;191;255m"
BRIGHT_YELLOW = "\033[38;2;255;255;0m"
BRIGHT_RED = "\033[38;2;255;69;0m"
BRIGHT_CYAN = "\033[38;2;0;255;255m"
BRIGHT_MAGENTA = "\033[38;2;255;0;255m"
BORDER_CHAR = "✦"

NUMBER_TYPE_MAPPING = {
    PhoneNumberType.FIXED_LINE: "Fixed Line",
    PhoneNumberType.MOBILE: "Mobile",
    PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
    PhoneNumberType.TOLL_FREE: "Toll Free",
    PhoneNumberType.PREMIUM_RATE: "Premium Rate",
    PhoneNumberType.SHARED_COST: "Shared Cost",
    PhoneNumberType.VOIP: "VoIP",
    PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
    PhoneNumberType.PAGER: "Pager",
    PhoneNumberType.UAN: "UAN",
    PhoneNumberType.VOICEMAIL: "Voicemail",
    PhoneNumberType.UNKNOWN: "Unknown"
}

def run():
    phone_number = input(f"{BRIGHT_RED}Entrez le numéro de téléphone (ex: +33749324574) : {Style.RESET_ALL}")

    try:
        parsed_number = phonenumbers.parse(phone_number)

        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        is_valid = phonenumbers.is_valid_number(parsed_number)
        status = f"{BRIGHT_GREEN}Valid{Style.RESET_ALL}" if is_valid else f"{BRIGHT_RED}Invalid{Style.RESET_ALL}"

        country_code = f"{BRIGHT_YELLOW}+{parsed_number.country_code}"

        country = geocoder.country_name_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "en")

        time_zones = timezone.time_zones_for_number(parsed_number)

        operator = carrier.name_for_number(parsed_number, "en")

        number_type = phonenumbers.number_type(parsed_number)
        number_type_str = NUMBER_TYPE_MAPPING.get(number_type, "Unknown")

        print(f"\n{BRIGHT_MAGENTA}{BORDER_CHAR * 40}")
        print(f"{BRIGHT_BLUE}[=] Phone Number   {BRIGHT_MAGENTA} » {BRIGHT_CYAN}{phone_number}")
        print(f"{BRIGHT_BLUE}[=] Formatted      {BRIGHT_MAGENTA} » {BRIGHT_YELLOW}{formatted_number}")
        print(f"{BRIGHT_BLUE}[=] Status         {BRIGHT_MAGENTA} » {status}")
        print(f"{BRIGHT_BLUE}[=] Country Code   {BRIGHT_MAGENTA} » {country_code}")
        print(f"{BRIGHT_BLUE}[=] Country        {BRIGHT_MAGENTA} » {BRIGHT_GREEN}{country}")
        print(f"{BRIGHT_BLUE}[=] Region         {BRIGHT_MAGENTA} » {BRIGHT_GREEN}{region}")
        print(f"{BRIGHT_BLUE}[=] Timezone       {BRIGHT_MAGENTA} » {BRIGHT_YELLOW}{', '.join(time_zones)}")
        print(f"{BRIGHT_BLUE}[=] Operator       {BRIGHT_MAGENTA} » {BRIGHT_CYAN}{operator or 'Unknown'}")
        print(f"{BRIGHT_BLUE}[=] Type Number    {BRIGHT_MAGENTA} » {BRIGHT_CYAN}{number_type_str}")
        print(f"{BRIGHT_MAGENTA}{BORDER_CHAR * 40}\n")

    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"{BRIGHT_RED}Erreur : Le numéro de téléphone n'est pas valide.")

if __name__ == "__main__":
    run()
