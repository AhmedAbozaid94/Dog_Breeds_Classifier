#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Ahmed Abozaid
# DATE CREATED: 7/9/2023
# REVISED DATE: 7/10/2023
def print_results(results_dic: dict, results_stats_dic: dict, model: str, 
                  print_incorrect_dogs: bool = False, print_incorrect_breed: bool = False) -> None:
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if the user indicates 
    they want those printouts (use non-default values).
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)
                    idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a percentage or a count) where the key is the statistic's 
                   name (starting with 'pct' for percentage or 'n' for count)
                   and the value is the statistic's value 
      model - Indicates which CNN model architecture was used by the 
              classifier function to classify the pet images. Values must be either: 
              resnet, alexnet, or vgg (string)
      print_incorrect_dogs - True to print incorrectly classified dog images, 
                             False to skip printing (default: False)
      print_incorrect_breed - True to print incorrectly classified dog breeds, 
                              False to skip printing (default: False)
    Returns:
           None - simply printing results.
    """   
    # Prints summary statistics over the run
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")
    print(f"{'N Images':20}: {results_stats_dic['n_images']:3d}")
    print(f"{'N Dog Images':20}: {results_stats_dic['n_dogs_img']:3d}")
    print(f"{'N Not-Dog Images':20}: {results_stats_dic['n_notdogs_img']:3d}")
    
    # Prints summary statistics (percentages) on Model Run
    print("\n")
    for key, value in results_stats_dic.items():
        if key.startswith('p'):
            print(f"{key.upper():25}: {value:.1f}%")
            
    # If print_incorrect_dogs is True and there were images incorrectly classified as dogs or vice versa
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        
        # Process through results dict, printing incorrectly classified dogs
        for key, value in results_dic.items():
            pet_label, classifier_label, is_match, is_dog, is_classifier_dog = value
            
            # Pet Image Label is a Dog and Classifier Label is NOT a Dog
            if is_dog == 1 and is_classifier_dog == 0:
                print(f"Pet Label: {pet_label:>26}   Classifier Label: {classifier_label:>30}")
            
            # Pet Image Label is NOT a Dog and Classifier Label is a Dog
            elif is_dog == 0 and is_classifier_dog == 1:
                print(f"Pet Label: {pet_label:>26}   Classifier Label: {classifier_label:>30}")
    
    # If print_incorrect_breed is True and there were dogs whose breeds were incorrectly classified
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nINCORRECT Dog Breed Assignment:")
        
        # Process through results dict, printing incorrectly classified breeds
        for key, value in results_dic.items():
            pet_label, classifier_label, is_match, is_dog, is_classifier_dog = value
            
            # Pet Image Label is a Dog, classified as a Dog, but is the WRONG breed
            if is_dog == 1 and is_classifier_dog == 1 and is_match == 0:
                print(f"Pet Label: {pet_label:>26}   Classifier Label: {classifier_label:>30}")