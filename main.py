from datetime import datetime as dt 
import pytz

def run():
    print("""
  ___ ___ _    ___     _   __  __ _   _ _  _ ___ ___   _   _    
 | _ \ __| |  / _ \ _ | | |  \/  | | | | \| |   \_ _| /_\ | |   
 |   / _|| |_| (_) | || | | |\/| | |_| | .` | |) | | / _ \| |__ 
 |_|_\___|____\___/ \__/  |_|  |_|\___/|_|\_|___/___/_/ \_\____|
 """)


    ecuador_tz = pytz.timezone('America/Guayaquil')
    ecuador_date = dt.now(ecuador_tz)
    print('🇪🇨Ecuador/Guayaquil: ', ecuador_date.strftime('📅 %d/%m/%Y 🕑 %H:%M:%S\n'))

    chile_tz = pytz.timezone('America/Santiago')
    chile_date = dt.now(chile_tz)
    print('🇨🇱Chile/Santiago: ', chile_date.strftime('   📅 %d/%m/%Y 🕑 %H:%M:%S\n'))

    Mexico_tz = pytz.timezone('America/Mexico_City')
    Mexico_date = dt.now(Mexico_tz)
    print('🇲🇽Mexico/CDMX: ', Mexico_date.strftime('      📅 %d/%m/%Y 🕑 %H:%M:%S\n'))

    usa_tz = pytz.timezone('America/New_York')
    usa_date = dt.now(usa_tz)
    print('🇺🇸USA/New York: ', usa_date.strftime('     📅 %d/%m/%Y 🕑 %H:%M:%S\n'))

    españa_tz = pytz.timezone('Europe/Madrid')
    españa_date = dt.now(españa_tz)
    print('🇪🇸España/Madrid: ', españa_date.strftime('    📅 %d/%m/%Y 🕑 %H:%M:%S\n'))

    





if __name__ == '__main__':
    run()