/*
Author: Tony Lindgren

Completed by : Maryam askari and Mahtab BabaMohammadi
*/

:- use_module([library(clpfd)]).

zebra:-
        % Define variabels and their domain      
        House_colors = [Red, Green, White, Yellow, Blue],
        Nationality = [English, German, Swede, Dane, Norwegian]
        Drinks = [Tea, Coffee, Milk, Beer, Water]
        Pet = [Cats, Dog, Birds, Horse]
        Smokes = [Pall_Mall, Dunhill, Blend, Blue_Master, Prince]

        domain(House_colors, 1, 5), 
        domain(Drinks, 1, 5), 
        domain(Pet, 1, 4), 
        domain(Smokes, 1, 5), 
        domain(Nationality, 1, 5), 

        % Define constraints and relations
        all_different(House_colors), 
        all_different(Drinks),
        all_different(Smokes),
        all_different(Pet),
        all_different(Nationality),   

        Red #= English,  
        Swede #= Dog,
        Dane #= Tea,
        Green #= White + 1,
        Coffee #= Green,
        Pall_Mall #= Birds,
        Yellow #= Dunhill,
        Milk #= 3,
        Norwegian #= 1,
        next_to(Blend, Cats),
        next_to(Horse, Dunhill),
        Blue_Master #= Beer,
        German #= Prince,
        next_to(Norwegian, Blue),
        next_to(Water, Blend),


        % append variables to one list
        append(House_colors, Nationality, Temp1),
        append(Temp1, Pet, Temp2),
        append(Temp2, Drinks, Temp3)
        append(Temp3, Smokes, VariableList),
       
        % find solution
        labeling([1, 2, 3, 4, 5], VariableList),  

        % connect answers with right objects
        sort([Red-red, Green-green, White-white, Yellow-yellow, Blue-blue], House_color_connection),
        sort([English-english, Swede-swede, Dane-dane, Norwegian-norwegian, German-german], Nation_connection), 
        sort([Tea-tea, Coffee-coffee, Milk-milk, Beer-beer, Water-water], Drink_connection), 
        sort([Cats-cats, Dog-dog, Birds-birds, Horse-horse], Pet_connection), 
        sort([Pall_Mall-pall_mall, Dunhill-dunhill, Blend-blend, Blue_Master-blue_master, Prince-prince], Smoke_connection), 

        % print solution
        Format = '~w~15|~w~30|~w~45|~w~60|~w~n',
        format(Format, ['house 1', 'house 2', 'house 3', 'house 4', 'house 5']),
        format(Format, House_color_connection),
        format(Format, Nation_connection),
        format(Format, Drink_connection),                                                          
        format(Format, Pet_connection), 
        format(Format, Smoke_connection).
            
        