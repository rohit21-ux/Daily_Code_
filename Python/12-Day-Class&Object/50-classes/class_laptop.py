class gaminglaptop:
    def __init__(self,
                 ml_brand:str,
                 ml_manufacturer:str,
                 ml_series:str,
                 ml_colour:str,
                 ml_formfactor:str,
                 ml_screendisplaysize:str,
                 ml_screenresolution:str,
                 ml_arebatteriesrequired:bool,
                 ml_modelnumber:str,
                 ml_processorbrand:str,
                 ml_ProcessorType:str,
                 ml_ProcessorSpeed:str,
                 ml_ProcessorCount:str,
                 ml_MemoryTechnology:str,
                 ml_ComputerMemoryType:str,
                 ml_MaximumMemorySupported:str,
                 ml_MemoryClockSpeed:str,
                 ml_GraphicsCardRamSize:int,
                 ml_HardDriveSize:str,
                 ml_HardDiskDescription:str,
                 ml_GraphicsCoprocessor:str,
                 ml_OperatingSystem:str,
                 ml_IncludedComponents:tuple,
                 ml_CountryofOrigin:str,
                 ml_ItemWeight:tuple,
                 ml_specialfeatures:str

                 ):
        self.brand=ml_brand
        self.manufacturer=ml_manufacturer
        self.series=ml_series
        self.colour=ml_colour
        self.formfactor=ml_formfactor
        self.screendisplaysize=ml_screendisplaysize
        self.screenresolution=ml_screenresolution
        self.arebatteriesrequired=ml_arebatteriesrequired
        self.modelnumber=ml_modelnumber
        self.processorbrand=ml_processorbrand
        self.ProcessorType=ml_ProcessorType
        self.ProcessorSpeed=ml_ProcessorSpeed
        self.ProcessorCount=ml_ProcessorCount
        self.MemoryTechnology=ml_MemoryTechnology
        self.ComputerMemoryType=ml_ComputerMemoryType
        self.MaximumMemorySupported=ml_MaximumMemorySupported
        self.MemoryClockSpeed=ml_MemoryClockSpeed
        self.GraphicsCardRamSize=ml_GraphicsCardRamSize
        self.HardDriveSize=ml_HardDriveSize
        self.HardDiskDescription=ml_HardDiskDescription
        self.GraphicsCoprocessor=ml_GraphicsCoprocessor
        self.OperatingSystem=ml_OperatingSystem
        self.IncludedComponents=ml_IncludedComponents
        self.CountryofOrigin=ml_CountryofOrigin
        self.ItemWeight=ml_ItemWeight
        self.specialfeatures=ml_specialfeatures


    def show(self):
         print(f'BrandName:{self.brand}')
         print(f'manufacturer:{self.manufacturer}')
         print(f'series:{self.series}')
         print(f'colour:{self.colour}')
         print(f'formfactor:{self.formfactor}')
         print(f'Screen Display Size: {self.screendisplaysize}')
         print(f'Screen Resolution: {self.screenresolution}')
         print(f'Batteries Required: {self.arebatteriesrequired}')
         print(f'Model Number: {self.modelnumber}')
         print(f'Processor Brand: {self.processorbrand}')
         print(f'Processor Type: {self.ProcessorType}')
         print(f'Processor Speed: {self.ProcessorSpeed}')
         print(f'Processor Count: {self.ProcessorCount}')
         print(f'Memory Technology: {self.MemoryTechnology}')
         print(f'Computer Memory Type: {self.ComputerMemoryType}')
         print(f'Maximum Memory Supported: {self.MaximumMemorySupported}')
         print(f'Memory Clock Speed: {self.MemoryClockSpeed}')
         print(f'Graphics Card RAM Size: {self.GraphicsCardRamSize} GB')
         print(f'Hard Drive Size: {self.HardDriveSize}')
         print(f'Hard Disk Description: {self.HardDiskDescription}')
         print(f'Graphics Coprocessor: {self.GraphicsCoprocessor}')
         print(f'Operating System: {self.OperatingSystem}')
         print(f'Included Components: {(self.IncludedComponents)}')
         print(f'Country of Origin: {self.CountryofOrigin}')
         print(f'Item Weight: {self.ItemWeight[0]} {self.ItemWeight[1]}')
         print(f'Special Features: {self.specialfeatures}')

mygaminglaptop=gaminglaptop( ml_brand='Lenovo',
    ml_manufacturer='Lenovo',
    ml_series='LOQ',
    ml_colour='Luna Gray',
    ml_formfactor='Laptop',
    ml_screendisplaysize='15.6 Inches',
    ml_screenresolution='1920 x 1080',
    ml_arebatteriesrequired=True,
    ml_modelnumber='82XV00F6IN',
    ml_processorbrand='Intel',
    ml_ProcessorType='Core i5',
    ml_ProcessorSpeed='4.5 GHz',
    ml_ProcessorCount='1',
    ml_MemoryTechnology='DDR5',
    ml_ComputerMemoryType='DDR5 SDRAM',
    ml_MaximumMemorySupported='16 GB',
    ml_MemoryClockSpeed='5200 MHz',
    ml_GraphicsCardRamSize=6,
    ml_HardDriveSize='512 GB',
    ml_HardDiskDescription='SSD',
    ml_GraphicsCoprocessor='NVIDIA GeForce RTX 4050',
    ml_OperatingSystem='Windows 11',
    ml_IncludedComponents=('Laptop', 'Power Adapter', 'User Manual'),
    ml_CountryofOrigin='China',
    ml_ItemWeight=(2.4, 'kg'),
    ml_specialfeatures='AI Engine + : The Lenovo AI Engine+ and Lenovo LA1 AI Chip work together with the MUX Switch with NVIDIA Advanced Optimus for a truly epic boost in performance'
)













mygaminglaptop.show()

        