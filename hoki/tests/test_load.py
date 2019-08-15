from hoki import load
import pkg_resources

data_path = pkg_resources.resource_filename('hoki', 'data')

sn_file = data_path+'/supernova-bin-imf_chab100.z008.dat'
nmbr_file = data_path+'/numbers-bin-imf_chab100.z001.dat'
yields_file = data_path+'/yields-bin-imf_chab100.z001.dat'
masses_file_sin = data_path+'/starmass-sin-imf_chab100.z006.dat'
masses_file_bin = data_path+'/starmass-bin-imf_chab100.z014.dat'
hr_file = data_path+'/hrs-sin-imf_chab100.zem4.dat'
sed_file = data_path+'/spectra-bin-imf135_300.z002.dat'
ion_file = data_path+'/ionizing-bin-imf135_300.z002.dat'
colour_file = data_path+'/colours-bin-imf135_300.z002.dat'

def test_model_output():
    data = load.model_output(sn_file)
    data = load.model_output(nmbr_file)
    data = load.model_output(yields_file)
    data = load.model_output(masses_file_bin)
    data = load.model_output(sed_file)
    data = load.model_output(ion_file)
    data = load.model_output(hr_file, hr_type='TL')
    data = load.model_output(hr_file, hr_type='Tg')
    data = load.model_output(hr_file, hr_type='TTG')
    del data


def test_load_sn_rates():
    data = load._sn_rates(sn_file)
    assert data.shape[0] > 0, "The DataFrame is empty"
    assert data.shape[1] == 18, "There should be 18 columns, instead there are "+str(data.shape[1])


def test_load_stellar_numbers():
    data = load._stellar_numbers(nmbr_file)
    assert data.shape[0] > 0, "The DataFrame is empty"
    assert data.shape[1] == 21, "There should be 21 columns, instead there are "+str(data.shape[1])


def test_load_yields():
    data = load._yields(yields_file)
    assert data.shape[0] > 0, "the dataframe is empty"
    assert data.shape[1] == 9, "there should be 9 columns, instead there are "+str(data.shape[1])


def test_load_stellar_masses_sin():
    data = load._stellar_masses(masses_file_sin)
    assert data.shape[0] > 0, "the dataframe is empty"
    assert data.shape[1] == 3, "there should be 3 columns, instead there are "+str(data.shape[1])


def test_load_stellar_masses_bin():
    data = load._stellar_masses(masses_file_bin)
    assert data.shape[0] > 0, "the dataframe is empty"
    assert data.shape[1] == 3, "there should be 3 columns, instead there are "+str(data.shape[1])


def test_load_hrTL():
    data = load._hrTL(hr_file)
    assert data.high_H.shape == (51, 100, 100), "Attribute high_H has the wrong shape"
    assert data.medium_H.shape == (51, 100, 100), "Attribute medium_H has the wrong shape"
    assert data.low_H.shape == (51, 100, 100), "Attribute low_H has the wrong shape"


def test_load_hrTg():
    data = load._hrTg(hr_file)
    assert data.high_H.shape == (51, 100, 100), "Attribute high_H has the wrong shape"
    assert data.medium_H.shape == (51, 100, 100), "Attribute medium_H has the wrong shape"
    assert data.low_H.shape == (51, 100, 100), "Attribute low_H has the wrong shape"


def test_load_hrTTG():
    data = load._hrTTG(hr_file)
    assert data.high_H.shape == (51, 100, 100), "Attribute high_H has the wrong shape"
    assert data.medium_H.shape == (51, 100, 100), "Attribute medium_H has the wrong shape"
    assert data.low_H.shape == (51, 100, 100), "Attribute low_H has the wrong shape"


def test_sed():
    data = load._sed(sed_file)
    assert data.shape[0] > 0, "the dataframe is empty"
    assert data.shape[1] == 52, "there should be 52 columns, instead there are "+str(data.shape[1])


def test_ion():
    data = load._ionizing_flux(ion_file)
    assert data.shape[0] > 0, "the dataframe is empty"
    assert data.shape[1] == 5, "there should be 5 columns, instead there are "+str(data.shape[1])


def test_colours():
    data = load._colours(colour_file)
    assert data.shape[0] > 0, "the dataframe is empty"
    assert data.shape[1] == 26, "there should be 26 columns, instead there are "+str(data.shape[1])