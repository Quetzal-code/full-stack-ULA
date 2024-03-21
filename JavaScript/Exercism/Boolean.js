export function canFreePrisoner(
    knightIsAwake,
    archerIsAwake,
    prisonerIsAwake,
    petDogIsPresent,
  ) {
   if(petDogIsPresent === true && canExecuteFastAttack(knightIsAwake) === true && canSignalPrisoner(archerIsAwake, prisonerIsAwake)=== true  || canSpy(knightIsAwake, archerIsAwake, prisonerIsAwake)=== false && petDogIsPresent === true || petDogIsPresent === false && canExecuteFastAttack(knightIsAwake) === true && canSignalPrisoner(archerIsAwake, prisonerIsAwake)=== true ||  knightIsAwake === true && archerIsAwake === false  && prisonerIsAwake === false && petDogIsPresent === true || canSignalPrisoner(archerIsAwake, prisonerIsAwake)=== true && petDogIsPresent === true ){
     return true
   }else{
     return false
   } ;
  }


  export function canSpy(knightIsAwake, archerIsAwake, prisonerIsAwake) {
    if(knightIsAwake===false && archerIsAwake===true && prisonerIsAwake===false || knightIsAwake===false && archerIsAwake===false && prisonerIsAwake===true || knightIsAwake===false && archerIsAwake===true && prisonerIsAwake===true || knightIsAwake===true && archerIsAwake===false && prisonerIsAwake===false || knightIsAwake===true && archerIsAwake===true && prisonerIsAwake===false ||knightIsAwake===true && archerIsAwake===true && prisonerIsAwake===true ||
      knightIsAwake===true && archerIsAwake===false && prisonerIsAwake===true){
      return true
    } else {
      return false
    };
  }
