/* -*- Mode:Prolog; coding:iso-8859-1; indent-tabs-mode:nil; prolog-indent-width:8; prolog-paren-indent:4; tab-width:8; -*- 
Constraint store

Author: Tony Lindgren

Completed by : Maryam askari and Mahtab BabaMohammadi
*/
:- use_module([library(clpfd)]).

zebra:-
        % Define variabels and their domain      
        House_colors = [Red, Green, White, Yellow, Blue],
        domain(House_colors, 1, 5),        
        % Define constraints and relations
        all_different(House_colors),       
        Red #= English,        
        % append variables to one list
        append(House_colors, Nationality, Temp1),
        append(Temp1, Pet, Temp2),
        append(Temp3, Smokes, VariableList),
        % find solution
        labeling([], VariableList),                                           
        % connect answers with right objects
        sort([Red-red, Green-green, White-white, Yellow-yellow, Blue-blue], House_color_connection),
        sort([English-english, Swede-swede, Dane-dane, Norwegian-norwegian, German-german], Nation_connection),        
        % print solution
        Format = '~w~15|~w~30|~w~45|~w~60|~w~n',
        format(Format, ['house 1', 'house 2', 'house 3', 'house 4', 'house 5']),
        format(Format, House_color_connection),
        format(Format, Nation_connection).                                                        

            
        