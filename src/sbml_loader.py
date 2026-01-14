import tellurium as te

def load_sbml(path):
    rr = te.loadSBMLModel(path)
    species = rr.getFloatingSpeciesIds()
    parameters = rr.getGlobalParameterIds()
    return rr, species, parameters
