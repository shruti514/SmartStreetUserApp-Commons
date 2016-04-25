//
//  LightsController.swift
//  ParseStarterProject-Swift
//
//  Created by Shrutee Gangras on 4/25/16.
//  Copyright © 2016 Parse. All rights reserved.
//

import UIKit
import Parse

class LightsController: UIViewController {
    
 
        
        
        
        override func viewDidLoad() {
            super.viewDidLoad()
            // Do any additional setup after loading the view, typically from a nib.
            
            /*   var query = PFQuery(className: "Interaction")
             
             query.getObjectInBackgroundWithId("KHTyejPc8j") { (object:PFObject?, error:NSError?) in
             if error != nil {
             print(error)
             } else if interact = object!{
             
             //interact["Type"] = "Music"
             // interact["status"] = true
             // interact.saveInBackground()
             
             // print(object!)
             
             //print(object!.objectForKey("Type")!)
             }
             }
             
             */
            
            
        }
        
        @IBAction func lightsOn(sender: AnyObject) {
            
            var query = PFQuery(className: "Interaction")
            
            query.getObjectInBackgroundWithId("KHTyejPc8j") { (object:PFObject?, error:NSError?) in
                if error != nil {
                    print(error)
                } else if let interact = object{
                    
                    //interact["Type"] = "Music"
                    interact["status"] = true
                    interact.saveInBackground()
                    
                    print(object!)
                    
                    //print(object!.objectForKey("Type")!)
                }
            }
            
        }
        
        
        
        @IBAction func lightsOff(sender: AnyObject) {
            var query = PFQuery(className: "Interaction")
            
            query.getObjectInBackgroundWithId("KHTyejPc8j") { (object:PFObject?, error:NSError?) in
                if error != nil {
                    print(error)
                } else if let interact = object{
                    interact["status"] = false
                    interact.saveInBackground()
                    
                    print(object!)
                    
                    //print(object!.objectForKey("Type")!)
                }
            }
            
            
        }
        override func didReceiveMemoryWarning() {
            super.didReceiveMemoryWarning()
            // Dispose of any resources that can be recreated.
        }
    }



