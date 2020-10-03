
Two main functions - `deid()` and `reid()`. 

`deid` is used for deidentification of data. It replaces information about people with fake information before it's transmitted over insecure networks. This function stores the mapping between real -> fake info by storing the identifying data in a file, which must be stored in a secure location.

It takes the following parameters:

  - config object
  - input file name (real data)
  - output file name (de-identified data)

The config object has the following properties:

  - idDbFile - Name of a file where identifying information is stored.
  - input.idFieldName - Name of the field that uniquely identifies a person.
  - input.fieldSpecs - Specification of field names and types that should be de-identified. This is a napping table of field-name to field-type. Type is one of:
  	- name
  	- ssn
  	- date
  	- address

The `reid` function replaces fake information produced in `deid` function with real information.

It takes the following parameters:

  - config object
  - input file name (de-identified data)
  - output file name (real data)

  - idDbFile - Name of a file where identifying information is stored.
  - output.idFieldName - Name of the field that uniquely identifies a person.
  - output.fieldSpecs - specification of field names and types that should be mapped back to re-identify a file.

