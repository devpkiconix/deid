import pandas as pd
import json

def reid(cfg, inFn, outFn):
    '''
The `reid` function replaces fake information produced in `deid` function with real information.

It takes the following parameters:

  - config object
  - input file name (de-identified data)
  - output file name (real data)

  - idDbFile - Name of a file where identifying information is stored.
  - output.idFieldName - Name of the field that uniquely identifies a person.
  - output.fieldSpecs - specification of field names and types that should be mapped back to re-identify a file.

    '''
    validateConfig(cfg)

    input = readInput(inFn)
    mapping = readDeidMapping(cfg['idDbFile'])
    (out, mapping) = restoreData(cfg, input, mapping)

    writeReidData(outFn, out)

    pass

def validateConfig(cfg):
    if cfg['idDbFile'] == None:
        raise InvalidConfig('idDbFile')
    if cfg['idFieldName'] == None:
        raise InvalidConfig('idFieldName')
    if cfg['fieldSpecs'] == None:
        raise InvalidConfig('fieldSpecs')
    pass


def restoreData(cfg, input, mapping):
    out = input.copy()
    fieldNames = [cfg['idFieldName']] + list(cfg['fieldSpecs'].keys())
    for attr, value in cfg['fieldSpecs'].items():
      out[attr] = mapping[attr]
            
    return (out, mapping)

readInput        = lambda inputFn: pd.read_csv(inputFn)
writeReidData    = lambda outFn, data: data.to_csv(outFn)
readDeidMapping = lambda inFn:  pd.read_pickle(inFn)
#lambda outFn, data: data.to_csv(outFn)
dropDupes = lambda cfg, input: input.drop_duplicates(subset=[cfg['idFieldName']])

class InvalidConfig(Exception): pass


if __name__ == "__main__":
    infile = './testdata.deid.csv'
    config_file = './config.json'
    with open(config_file) as f:
      cfg = json.load(f)
    outfile = 'testdata.reid.csv'
    print(cfg, infile, outfile)
    reid(cfg, infile, outfile)
    print("DONE")


    cfg = {
        'idDbFile': './iddb.pkl',
        'idFieldName': 'id',
        'fieldSpecs': {
            'Name': 'name',
            'DOB': 'date',
            'SSN': 'ssn',
            'Address': 'address',
        },     
    }
