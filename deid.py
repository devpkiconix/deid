import pandas as pd
import json

from faker import Faker

fake = Faker()

def deid(config, inFn, outFn):
    '''
`deid` is used for deidentification of data. It replaces information about people with fake information before it's transmitted over insecure networks. This function stores the mapping between real -> fake info by storing the identifying data in a file, which must be stored in a secure location.

It takes the following parameters:

  - config object
  - input file name (real data)
  - output file name (de-identified data)

The config object has the following properties:

  - idDbFile - Name of a file where identifying information is stored.
  - idFieldName - Name of the field that uniquely identifies a person.
  - fieldSpecs - Specification of field names and types that should be de-identified.

The `reid` function replaces fake information produced in `deid` function with real information.    
    '''

    # Validate config
    # Read input file
    # Replace data with fake data
    # Write output file
    # Write mapping file
    validateConfig(cfg)

    input = readInput(inFn)
    deduped = dropDupes(cfg, input)
    (out, mapping) = replaceIdData(cfg, deduped)

    writeDeidData(outFn, out)
    writeDeidMapping(cfg['idDbFile'], mapping)
    pass


def validateConfig(cfg):
    if cfg['idDbFile'] == None:
        raise InvalidConfig('idDbFile')
    if cfg['idFieldName'] == None:
        raise InvalidConfig('idFieldName')
    if cfg['fieldSpecs'] == None:
        raise InvalidConfig('fieldSpecs')
    pass


def replaceIdData(cfg, input):
    out = input.copy()
    fieldNames = [cfg['idFieldName']] + list(cfg['fieldSpecs'].keys())
    mapping = input[fieldNames]
    for attr, value in cfg['fieldSpecs'].items():
        if value == 'name':
            out[attr] = out.apply(lambda row: fake.name(), axis=1)
        if value == 'ssn':
            out[attr] = out.apply(lambda row: fake.ssn(), axis=1)
        if value == 'date':
            out[attr] = out.apply(lambda row: fake.date(), axis=1)
        if value == 'address':
            out[attr] = out.apply(lambda row: fake.street_address(), axis=1)
            
    return (out, mapping)

readInput        = lambda inputFn: pd.read_csv(inputFn)
writeDeidData    = lambda outFn, data: data.to_csv(outFn)
writeDeidMapping = lambda outFn, df:  pd.to_pickle(df, outFn)
#lambda outFn, data: data.to_csv(outFn)
dropDupes = lambda cfg, input: input.drop_duplicates(subset=[cfg['idFieldName']])

class InvalidConfig(Exception): pass


if __name__ == "__main__":
    infile = './testdata.csv'
    config_file = './config.json'
    with open(config_file) as f:
      cfg = json.load(f)
    outfile = 'testdata.deid.csv'
    print(cfg, infile, outfile)
    deid(cfg, infile, outfile)
    print("DONE")