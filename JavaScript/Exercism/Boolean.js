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
  