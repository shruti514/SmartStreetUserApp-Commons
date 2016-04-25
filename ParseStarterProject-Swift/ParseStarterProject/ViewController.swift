/**
* Copyright (c) 2015-present, Parse, LLC.
* All rights reserved.
*
* This source code is licensed under the BSD-style license found in the
* LICENSE file in the root directory of this source tree. An additional grant
* of patent rights can be found in the PATENTS file in the same directory.
*/

import UIKit
import Parse

class ViewController: UIViewController {
    


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
