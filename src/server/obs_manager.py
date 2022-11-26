import logging

logger = logging.getLogger(__name__)

class NoOBSManager():
    def __init__(self):
        pass

    def isEnabled(self):
        return False

    def start(self):
        return True

    def stop(self):
        return True

class OBSManager():
    rc = None
    obsModule = None
    config = {} 
    
    def __init__(self, config, obsModule):
        self.config=config
        self.obsModule = obsModule
        self.connect()
        
    def connect(self):
        try:        
            logger.info("OBS: (Re)connecting...")
            self.rc = self.obsModule.ReqClient(host=self.config['HOST'], port=self.config['PORT'], password=self.config['PASSWORD'])        
        except:
            logger.error("OBS: Error connecting to configured instance")


    def isEnabled(self):
        return True

    def start(self):
        try:
            self.rc.start_record()
            logger.info("OBS: Recording Started")
        except:
            self.connect()          
            try:
                self.rc.start_record()
                logger.info("OBS: Recording Started")
            except:
                logger.error("OBS: Start Recording Failed")
                return False    
        return True

    def stop(self):
        try:
            self.rc.stop_record()
            logger.info("OBS: Recording Stoppped")
        except:
            self.connect()          
            try:
                self.rc.stop_record()
                logger.info("OBS: Recording Stoppped")
            except:
                logger.error("OBS: Stop Recording Failed")
                return False
        return True