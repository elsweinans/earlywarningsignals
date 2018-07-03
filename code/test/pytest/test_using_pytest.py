from pytest import approx, raises
import numpy as np
import pandas as pd

def test_dummy_pass():
    assert True

def test_dummy_fail():
    assert False
    
def test_logtransform():
    
    from earlywarningsignals import logtransform
    
    # Test 1. Trying a known value
    
    # Input and expected output
    x_in = pd.DataFrame(data=[0])
    y_computed = logtransform(x_in)
    y_expected = pd.DataFrame(data=[0.0])
    
    # Check it
    assert (y_computed.equals(y_expected))
    
    # Test 2. Trying a known value
    
    # Input and expected output
    x_in = pd.DataFrame(data=[1.0]) 
    y_computed = logtransform(x_in)
    y_expected = pd.DataFrame(data=[0.69314718055994529])
    
    # Check it
    assert (y_computed.equals(y_expected))
    
def test_EWS():
    from earlywarningsignals import EWS
    
    # Test 1. Trying a known value
    np_input_ts=np.array([[1,6],[3,5],[4,4],[6,1]])
    input_ts=pd.DataFrame(data=np_input_ts)
    output_autocorrelation=[0.92857142857142838, 0.96076892283052284]
    output_variance=[3.25, 3.5]
    output_skewness=[0.0, -0.6872431934890912]
    output_CV=[0.51507875363771272, 0.46770717334674267]
    output_kurtosis=[-1.1479289940828403, -1.0]
    result=EWS(input_ts,autocorrelation=True,variance=True,skewness=True,
               kurtosis=True,CV=True)
    assert(result['autocorrelation'] == output_autocorrelation)
    assert(result['variance'] == output_variance)
    assert(result['skewness'] == output_skewness)
    assert(result['kurtosis'] == output_kurtosis)
    assert(result['CV'] == output_CV)
    
def test_spaced():
    from earlywarningsignals import checkSpacing
    
    # Test 1: Trying a known value
    input_1 = np.reshape(np.arange(10),(10,1))
    input_2 = np.random.randint(low=0, high=10, size=(10,1))
    spaced_1 = input_1[1:]-input_1[0:-1]
    spaced_2 =  input_2[1:]-input_2[0:-1]
    output_1= True
    output_2= False
    
    assert(checkSpacing(spaced_1) == output_1)
    assert(checkSpacing(spaced_2) == output_2)
    
def test_timeseries():
    from earlywarningsignals import check_time_series
    
    # Test 1: Trying a known value
    input_1a = np.arange(10)*2
    input_1b = np.arange(10)
    input_2a = np.array([[1,6],[3,5],[4,4],[6,1]])
    input_2aa = np.array([['a','b'],['b','x'],['l','i'],['g','z']])
    input_2b = np.arange(4)
    input_2bb = np.random.randint(low=0, high=14, size=(4,1))
    input_3a = pd.DataFrame(input_1a)
    input_3b = pd.DataFrame(input_1b)
    input_4a = pd.DataFrame(input_2a)
    input_4b = pd.DataFrame(input_2b)
    [output_1a, output_1b] = check_time_series(input_1a)
    #still have to write asserts
    assert(isinstance(output_1a, pd.DataFrame))
    
    #check if evenly spaced check works
    with raises(ValueError):
        check_time_series(input_2a, input_2bb)
        
    #check if check if timeseries and timeindex have same length works
    with raises(ValueError):
        check_time_series(input_3a, input_4b)
    
    
    
    
    
    
    
    